
"""
Matrix-free Euclidean + physical-metric adjoint for the v1.1 full holomorphic pilot.

Features
--------
- analytic sparse face Jacobians for WENO7-JS;
- exact VJP of conservative LF-WENO7 transport;
- exact adjoint elliptic solve A^{-T};
- exact reverse-mode SSPRK3 step;
- physical kinetic-energy metric in (Gamma,Omega):
    E_G = 2*pi int Gamma^2/r dr dz
    E_O = 2*pi int r^3 psi1 Omega dr dz
  with -L5 psi1 = Omega.
- exact O(N) metric inverse using weighted self-adjointness of the discrete elliptic operator;
- 4-way tangent switches s12/s21 matching the project ablation convention;
- finite-window matrix-free forward / Euclidean transpose / metric adjoint;
- power iteration for the top physical-energy singular gain.

Important:
The r^3 factor in E_O is NOT a 5D physical volume measure.  It is the discrete
streamfunction identity equivalent in the continuum to the physical meridional kinetic
energy 2*pi int r[(u^r)^2+(u^z)^2] dr dz after integration by parts.
"""
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import importlib.util, sys, math
from pathlib import Path

_H=Path(__file__).with_name("mns2_full_holomorphic_pilot_v1.1.py")
_s=importlib.util.spec_from_file_location("_fp11_adj",_H)
h=importlib.util.module_from_spec(_s);sys.modules[_s.name]=h;_s.loader.exec_module(h)
c=h.c

B7=c.v10.B7 if hasattr(c,"v10") else None
Q7=c.v10.Q7 if hasattr(c,"v10") else None
D7=c.v10.D7 if hasattr(c,"v10") else None
if B7 is None:
    B7=c.v10.B7; Q7=c.v10.Q7; D7=c.v10.D7

def _pad_map(n,lp=1,rp=1,ng=4):
    ids=list(range(ng-1,-1,-1))+list(range(n))+list(range(n-1,n-ng-1,-1))
    sgn=[lp]*ng+[1]*n+[rp]*ng
    return np.array(ids,dtype=int),np.array(sgn,dtype=float)

def _face_grad(vals,eps_abs):
    q=np.einsum("fki,ki->fk",vals,Q7)
    beta=np.einsum("fki,kij,fkj->fk",vals,B7,vals)
    den=beta+eps_abs
    alpha=D7[None,:]/den**2
    asum=np.sum(alpha,axis=1,keepdims=True)
    w=alpha/asum
    face=np.sum(w*q,axis=1)
    cb=((q-face[:,None])/asum)*(-2*alpha/den)
    grad=w[:,:,None]*Q7[None,:,:] + cb[:,:,None]*(2*np.einsum("kij,fkj->fki",B7,vals))
    return grad

def reflected_left_jacobian(f,lp=1,rp=1,eps_abs=1e-6):
    f=np.asarray(f); n=f.size
    pids,psgn=_pad_map(n,lp,rp,4)
    a=psgn*f[pids]
    i=np.arange(n+1); j=i-1; p=j+4
    ids=[
        np.stack([p-3,p-2,p-1,p],axis=-1),
        np.stack([p-2,p-1,p,p+1],axis=-1),
        np.stack([p-1,p,p+1,p+2],axis=-1),
        np.stack([p,p+1,p+2,p+3],axis=-1),
    ]
    vals=np.stack([a[ii] for ii in ids],axis=1)
    grad=_face_grad(vals,eps_abs)
    rows=[];cols=[];data=[]
    for F in range(n+1):
        for k in range(4):
            for ell in range(4):
                pp=ids[k][F,ell]
                rows.append(F); cols.append(int(pids[pp])); data.append(float(np.real(grad[F,k,ell]*psgn[pp])))
    return sp.csr_matrix((data,(rows,cols)),shape=(n+1,n))

def reflected_lr_jacobians(f,lp=1,rp=1,eps_abs=1e-6):
    JL=reflected_left_jacobian(f,lp,rp,eps_abs)
    JRrev=reflected_left_jacobian(np.asarray(f)[::-1],rp,lp,eps_abs)
    n=len(f)
    JR=JRrev[np.arange(n,-1,-1),:][:,np.arange(n-1,-1,-1)]
    return JL.tocsr(),JR.tocsr()

def periodic_left_jacobian(f,eps_abs=1e-6):
    f=np.asarray(f);n=f.size;i=np.arange(n);j=i-1
    ids=[
        np.stack([(j-3)%n,(j-2)%n,(j-1)%n,j%n],axis=-1),
        np.stack([(j-2)%n,(j-1)%n,j%n,(j+1)%n],axis=-1),
        np.stack([(j-1)%n,j%n,(j+1)%n,(j+2)%n],axis=-1),
        np.stack([j%n,(j+1)%n,(j+2)%n,(j+3)%n],axis=-1),
    ]
    vals=np.stack([f[ii] for ii in ids],axis=1)
    grad=_face_grad(vals,eps_abs)
    rows=[];cols=[];data=[]
    for F in range(n):
        for k in range(4):
            for ell in range(4):
                rows.append(F);cols.append(int(ids[k][F,ell]));data.append(float(np.real(grad[F,k,ell])))
    return sp.csr_matrix((data,(rows,cols)),shape=(n,n))

def periodic_lr_jacobians(f,eps_abs=1e-6):
    JL=periodic_left_jacobian(f,eps_abs)
    Jrev=periodic_left_jacobian(np.asarray(f)[::-1],eps_abs)
    n=len(f)
    base=Jrev[np.arange(n-1,-1,-1),:][:,np.arange(n-1,-1,-1)]
    JR=base[(np.arange(n)-1)%n,:]
    return JL.tocsr(),JR.tocsr()

def corner_flux_vjp(pqr,pqz,dr,dz):
    pPhi=(pqr-np.roll(pqr,1,axis=1))/dz
    pPhi[:-1,:]-=pqz/dr
    pPhi[1:,:]+=pqz/dr
    return pPhi

def transport_vjp(f,Phi,pout,r,dr,dz,alpha_r,alpha_z,eps_abs,
                  radial_lp=1,radial_rp=-1):
    """Euclidean transpose of c.rhs wrt (f,Phi)."""
    f=np.asarray(f); nr,nz=f.shape
    qr,qz=c.corner_fluxes(Phi,dr,dz)
    pdiv=-pout/r[:,None]
    pHr=np.zeros((nr+1,nz),dtype=float)
    pHr[:-1,:]-=pdiv/dr
    pHr[1:,:]+=pdiv/dr
    pHr[0,:]=0; pHr[-1,:]=0
    pHz=(np.roll(pdiv,1,axis=1)-pdiv)/dz
    rf=np.arange(nr+1)*dr
    Lr=np.empty((nr+1,nz));Rr=np.empty_like(Lr)
    pf=np.zeros_like(f,dtype=float)
    pqr=np.zeros_like(qr,dtype=float)
    for j in range(nz):
        Lr[:,j],Rr[:,j],_,_=c.reflected_lr_faces_and_jvp(
            f[:,j],np.zeros(nr),radial_lp,radial_rp,eps_abs)
        JL,JR=reflected_lr_jacobians(f[:,j],radial_lp,radial_rp,eps_abs)
        pL=.5*(qr[:,j]+alpha_r*rf)*pHr[:,j]
        pR=.5*(qr[:,j]-alpha_r*rf)*pHr[:,j]
        pf[:,j]+=JL.T@pL+JR.T@pR
        pqr[:,j]+=.5*(Lr[:,j]+Rr[:,j])*pHr[:,j]
    Lz=np.empty((nr,nz));Rz=np.empty_like(Lz)
    pqz=np.zeros_like(qz,dtype=float)
    for i in range(nr):
        Lz[i],Rz[i],_,_=c.periodic_lr_faces_and_jvp(f[i],np.zeros(nz),eps_abs)
        JL,JR=periodic_lr_jacobians(f[i],eps_abs)
        pL=.5*(qz[i]+alpha_z*r[i])*pHz[i]
        pR=.5*(qz[i]-alpha_z*r[i])*pHz[i]
        pf[i]+=JL.T@pL+JR.T@pR
        pqz[i]+=.5*(Lz[i]+Rz[i])*pHz[i]
    pPhi=corner_flux_vjp(pqr,pqz,dr,dz)
    return pf,pPhi

class AdjointPilot(h.FullPilot):
    def __init__(self,*a,**kw):
        super().__init__(*a,**kw)
        self.solve_adj_real=spla.factorized(self.A.T.tocsc())
        self._metric_c=2*math.pi*self.dr*self.dz

    def phi_vjp(self,pPhi):
        rf=np.arange(self.nr+1)*self.dr
        ppc=rf[:,None]**2*pPhi
        pz=np.zeros((self.nr,self.nz),dtype=float)
        pz[:-1]+=0.5*ppc[1:self.nr]
        pz[1:]+=0.5*ppc[1:self.nr]
        ppsi=.5*(pz+np.roll(pz,-1,axis=1))
        return self.solve_adj_real(ppsi.ravel()).reshape(self.nr,self.nz)

    def apply_L5_T(self,p):
        return -(self.A.T @ np.asarray(p).ravel()).reshape(self.nr,self.nz)

    def rhs_vjp(self,gamma,omega,pg,po,frozen,s12=1,s21=1):
        psi,Phi,_,_=self.reconstruct(omega)
        qg,pPhi_g=transport_vjp(gamma,Phi,pg,self.r,self.dr,self.dz,
                                frozen["alpha_r"],frozen["alpha_z"],frozen["eps_g"])
        if not s12:
            pPhi_g*=0
        qo,pPhi_o=transport_vjp(omega,Phi,po,self.r,self.dr,self.dz,
                                frozen["alpha_r"],frozen["alpha_z"],frozen["eps_o"])
        if s21:
            U=self.U(gamma); Uz=h.periodic_dz(U,self.dz)
            pU=2*po*Uz - h.periodic_dz(2*po*U,self.dz)
            qg+=pU/(self.r[:,None]**2)
        qg+=self.nu*self.apply_L5_T((self.r[:,None]**2)*pg)/(self.r[:,None]**2)
        qo+=self.nu*self.apply_L5_T(po)
        qo+=self.phi_vjp(pPhi_g+pPhi_o)
        return qg,qo

    def rhs_and_jvp_switched(self,gamma,omega,qg,qo,frozen,s12=1,s21=1):
        psi,Phi,_,_=self.reconstruct(omega)
        qpsi,qPhi,_,_=self.reconstruct(qo)
        ag,tg=c.rhs_and_jvp(gamma,Phi,qg,qPhi if s12 else np.zeros_like(qPhi),
                            self.r,self.dr,self.dz,frozen["alpha_r"],frozen["alpha_z"],
                            frozen["eps_g"])
        ao,to=c.rhs_and_jvp(omega,Phi,qo,qPhi,self.r,self.dr,self.dz,
                            frozen["alpha_r"],frozen["alpha_z"],frozen["eps_o"])
        U=self.U(gamma); qU=self.U(qg)
        Uz=h.periodic_dz(U,self.dz); qUz=h.periodic_dz(qU,self.dz)
        src=2*U*Uz
        qsrc=2*(qU*Uz+U*qUz) if s21 else np.zeros_like(U)
        dg=self.r[:,None]**2*self.apply_L5(U)
        qdg=self.r[:,None]**2*self.apply_L5(qU)
        do=self.apply_L5(omega); qdo=self.apply_L5(qo)
        rg=ag+self.nu*dg
        ro=ao+src+self.nu*do
        jg=tg+self.nu*qdg
        jo=to+qsrc+self.nu*qdo
        return rg,ro,jg,jo

    def step_jvp_switched(self,g,o,qg,qo,dt,frozen,s12=1,s21=1):
        r1g,r1o,j1g,j1o=self.rhs_and_jvp_switched(g,o,qg,qo,frozen,s12,s21)
        g1=g+dt*r1g;o1=o+dt*r1o;qg1=qg+dt*j1g;qo1=qo+dt*j1o
        r2g,r2o,j2g,j2o=self.rhs_and_jvp_switched(g1,o1,qg1,qo1,frozen,s12,s21)
        g2=.75*g+.25*(g1+dt*r2g);o2=.75*o+.25*(o1+dt*r2o)
        qg2=.75*qg+.25*(qg1+dt*j2g);qo2=.75*qo+.25*(qo1+dt*j2o)
        r3g,r3o,j3g,j3o=self.rhs_and_jvp_switched(g2,o2,qg2,qo2,frozen,s12,s21)
        gn=(g+2*(g2+dt*r3g))/3;on=(o+2*(o2+dt*r3o))/3
        qgn=(qg+2*(qg2+dt*j3g))/3;qon=(qo+2*(qo2+dt*j3o))/3
        return gn,on,qgn,qon

    def step_vjp(self,g,o,pg_out,po_out,dt,frozen,s12=1,s21=1):
        r1g,r1o=self.rhs(g,o,frozen)
        g1=g+dt*r1g;o1=o+dt*r1o
        r2g,r2o=self.rhs(g1,o1,frozen)
        g2=.75*g+.25*(g1+dt*r2g);o2=.75*o+.25*(o1+dt*r2o)
        pg=pg_out/3; po=po_out/3
        py2g=2*pg_out/3; py2o=2*po_out/3
        rg,ro=self.rhs_vjp(g2,o2,py2g,py2o,frozen,s12,s21)
        py2g=py2g+dt*rg; py2o=py2o+dt*ro
        pg+=.75*py2g; po+=.75*py2o
        py1g=.25*py2g; py1o=.25*py2o
        rg,ro=self.rhs_vjp(g1,o1,py1g,py1o,frozen,s12,s21)
        py1g=py1g+dt*rg; py1o=py1o+dt*ro
        pg+=py1g; po+=py1o
        rg,ro=self.rhs_vjp(g,o,py1g,py1o,frozen,s12,s21)
        pg+=dt*rg; po+=dt*ro
        return pg,po

    def metric_apply(self,g,o):
        mg=self._metric_c*g/self.r[:,None]
        psi=self.solve_psi(o)
        mo=self._metric_c*(self.r[:,None]**3)*psi
        return mg,mo

    def metric_solve(self,bg,bo):
        g=bg*self.r[:,None]/self._metric_c
        psi=bo/(self._metric_c*(self.r[:,None]**3))
        o=(self.A@psi.ravel()).reshape(self.nr,self.nz)
        return g,o

    def metric_inner(self,a,b):
        ag,ao=a;bg,bo=b
        mbg,mbo=self.metric_apply(bg,bo)
        return float(np.sum(ag*mbg)+np.sum(ao*mbo))

    def metric_norm(self,a):
        return math.sqrt(max(self.metric_inner(a,a),0.0))

    def step_metric_adjoint(self,g,o,pg,po,dt,frozen,s12=1,s21=1):
        mpg,mpo=self.metric_apply(pg,po)
        eg,eo=self.step_vjp(g,o,mpg,mpo,dt,frozen,s12,s21)
        return self.metric_solve(eg,eo)

class WindowPropagator:
    def __init__(self,P,g0,o0,dt,nsteps,frozen,s12=1,s21=1):
        self.P=P;self.dt=dt;self.nsteps=nsteps;self.frozen=frozen
        self.s12=s12;self.s21=s21
        self.states=[(g0.copy(),o0.copy())]
        g,o=g0.copy(),o0.copy()
        for _ in range(nsteps):
            g,o=P.ssprk3_step(g,o,dt,frozen)
            self.states.append((g.copy(),o.copy()))

    def matvec(self,q):
        qg,qo=q
        for k in range(self.nsteps):
            g,o=self.states[k]
            _,_,qg,qo=self.P.step_jvp_switched(g,o,qg,qo,self.dt,self.frozen,self.s12,self.s21)
        return qg,qo

    def rmatvec_euclid(self,p):
        pg,po=p
        for k in range(self.nsteps-1,-1,-1):
            g,o=self.states[k]
            pg,po=self.P.step_vjp(g,o,pg,po,self.dt,self.frozen,self.s12,self.s21)
        return pg,po

    def rmatvec_metric(self,p):
        pg,po=self.P.metric_apply(*p)
        pg,po=self.rmatvec_euclid((pg,po))
        return self.P.metric_solve(pg,po)

def top_singular_power(T,seed=1234,maxiter=80,tol=1e-10):
    P=T.P; rng=np.random.default_rng(seed)
    q=(rng.normal(size=T.states[0][0].shape),rng.normal(size=T.states[0][1].shape))
    n=P.metric_norm(q);q=(q[0]/n,q[1]/n)
    sigma=0.0
    for it in range(maxiter):
        y=T.matvec(q); sn=P.metric_norm(y)
        z=T.rmatvec_metric(y); zn=P.metric_norm(z)
        qn=(z[0]/zn,z[1]/zn)
        ov=abs(P.metric_inner(q,qn))
        q=qn
        if abs(sn-sigma)<=tol*max(1.0,sn) and 1-ov<10*tol:
            sigma=sn;break
        sigma=sn
    return sigma,q,it+1
