
"""
Full holomorphic pilot for the Hou (Gamma, Omega) variables — v1.1.

Purpose
-------
Integrate the v1.1 conservative LF-WENO7 transport with:
- a cell-centered periodic-z elliptic solve for -L5 psi1 = Omega;
- compatible physical 3D face fluxes from Phi = r^2 psi1;
- Gamma diffusion through Gamma=r^2 U, L_- Gamma = r^2 L5 U;
- Omega source 2 U U_z;
- SSPRK3 base step and exact stage-by-stage JVP.

This is a differentiability / discrete-structure pilot only.
The wall-vorticity closure is homogeneous Dirichlet in this pilot and is NOT Hou's
production no-slip wall-vorticity treatment.
"""
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import importlib.util, sys
from pathlib import Path

_C = Path(__file__).with_name("mns2_conservative_lf_weno7_holomorphic_v1.1.py")
_s = importlib.util.spec_from_file_location("_mns2_c11",_C)
c = importlib.util.module_from_spec(_s); sys.modules[_s.name]=c; _s.loader.exec_module(c)

def build_minus_L5(nr,nz):
    dr=1.0/nr; dz=1.0/nz
    r=(np.arange(nr)+0.5)*dr
    rows=[]; cols=[]; vals=[]
    def idx(i,j): return i*nz+(j%nz)
    for i in range(nr):
        ri=r[i]
        rm=i*dr; rp=(i+1)*dr
        # radial L5 finite-volume coefficients
        if i>0:
            cm=rm**3/(dr**2*ri**3)
        else:
            cm=0.0
        if i<nr-1:
            cp=rp**3/(dr**2*ri**3)
            c0r=-(cm+cp)
        else:
            # Dirichlet value zero at wall face, half-cell distance -> gradient -2 f_i/dr
            wall=2.0*rp**3/(dr**2*ri**3)
            cp=0.0
            c0r=-(cm+wall)
        cz=1.0/dz**2
        # A=-L5
        row=idx(i,0)  # dummy overwritten per j
        for j in range(nz):
            row=idx(i,j)
            rows.append(row); cols.append(row); vals.append(-(c0r-2*cz))
            if i>0:
                rows.append(row); cols.append(idx(i-1,j)); vals.append(-cm)
            if i<nr-1:
                rows.append(row); cols.append(idx(i+1,j)); vals.append(-cp)
            rows += [row,row]
            cols += [idx(i,j-1),idx(i,j+1)]
            vals += [-cz,-cz]
    A=sp.csr_matrix((vals,(rows,cols)),shape=(nr*nz,nr*nz))
    return A,r,dr,dz

def periodic_dz(f,dz):
    return (np.roll(f,-1,axis=1)-np.roll(f,1,axis=1))/(2*dz)

class FullPilot:
    def __init__(self,nr,nz,nu=5e-3,alpha_safety=1.30,eps0=1e-6):
        self.A,self.r,self.dr,self.dz=build_minus_L5(nr,nz)
        self.solve_real=spla.factorized(self.A.tocsc())
        self.nr,self.nz,self.nu=nr,nz,nu
        self.alpha_safety=alpha_safety; self.eps0=eps0

    def solve_psi(self,omega):
        b=np.asarray(omega).ravel()
        if np.iscomplexobj(b):
            return (self.solve_real(np.real(b))+1j*self.solve_real(np.imag(b))).reshape(self.nr,self.nz)
        return self.solve_real(b).reshape(self.nr,self.nz)

    def apply_L5(self,f):
        return -(self.A @ np.asarray(f).ravel()).reshape(self.nr,self.nz)

    def phi_from_psi(self,psi):
        # psi at cell centers -> Phi=r_face^2 psi at (radial face, periodic z face)
        zface=0.5*(np.roll(psi,1,axis=1)+psi)   # face j between cells j-1 and j
        pc=np.zeros((self.nr+1,self.nz),dtype=psi.dtype)
        pc[1:self.nr,:]=0.5*(zface[:-1,:]+zface[1:,:])
        pc[0,:]=zface[0,:]       # multiplied by r^2=0
        pc[-1,:]=0.0             # psi=0 at wall
        rf=np.arange(self.nr+1)*self.dr
        return rf[:,None]**2*pc

    def reconstruct(self,omega):
        psi=self.solve_psi(omega)
        Phi=self.phi_from_psi(psi)
        qr,qz=c.corner_fluxes(Phi,self.dr,self.dz)
        rf=np.arange(self.nr+1)*self.dr
        ur=np.zeros_like(qr)
        ur[1:]=qr[1:]/rf[1:,None]
        uz=qz/self.r[:,None]
        return psi,Phi,ur,uz

    def U(self,gamma):
        return gamma/(self.r[:,None]**2)

    def freeze_constants(self,gamma,omega,safety=None):
        _,Phi,_,_=self.reconstruct(omega)
        ar,az,_,_=c.alpha_envelope_real(Phi,self.r,self.dr,self.dz,
                                        self.alpha_safety if safety is None else safety)
        sg=max(float(np.max(np.abs(gamma))),1.0)
        so=max(float(np.max(np.abs(omega))),1.0)
        return dict(alpha_r=ar,alpha_z=az,
                    eps_g=c.frozen_eps(sg,self.eps0),
                    eps_o=c.frozen_eps(so,self.eps0))

    def rhs_and_jvp(self,gamma,omega,qg,qo,frozen):
        psi,Phi,_,_=self.reconstruct(omega)
        qpsi,qPhi,_,_=self.reconstruct(qo)

        ag,tg=c.rhs_and_jvp(gamma,Phi,qg,qPhi,self.r,self.dr,self.dz,
                            frozen["alpha_r"],frozen["alpha_z"],frozen["eps_g"],
                            radial_lp=1,radial_rp=-1)
        ao,to=c.rhs_and_jvp(omega,Phi,qo,qPhi,self.r,self.dr,self.dz,
                            frozen["alpha_r"],frozen["alpha_z"],frozen["eps_o"],
                            radial_lp=1,radial_rp=-1)

        U=self.U(gamma); qU=self.U(qg)
        Uz=periodic_dz(U,self.dz); qUz=periodic_dz(qU,self.dz)
        src=2*U*Uz
        qsrc=2*(qU*Uz+U*qUz)

        dg=self.r[:,None]**2*self.apply_L5(U)
        qdg=self.r[:,None]**2*self.apply_L5(qU)
        do=self.apply_L5(omega)
        qdo=self.apply_L5(qo)

        rg=ag+self.nu*dg
        ro=ao+src+self.nu*do
        jg=tg+self.nu*qdg
        jo=to+qsrc+self.nu*qdo
        return rg,ro,jg,jo

    def rhs(self,gamma,omega,frozen):
        z=np.zeros_like(gamma)
        rg,ro,_,_=self.rhs_and_jvp(gamma,omega,z,z,frozen)
        return rg,ro

    def ssprk3_step_and_jvp(self,g,o,qg,qo,dt,frozen):
        r1g,r1o,j1g,j1o=self.rhs_and_jvp(g,o,qg,qo,frozen)
        g1=g+dt*r1g; o1=o+dt*r1o; qg1=qg+dt*j1g; qo1=qo+dt*j1o

        r2g,r2o,j2g,j2o=self.rhs_and_jvp(g1,o1,qg1,qo1,frozen)
        g2=.75*g+.25*(g1+dt*r2g); o2=.75*o+.25*(o1+dt*r2o)
        qg2=.75*qg+.25*(qg1+dt*j2g); qo2=.75*qo+.25*(qo1+dt*j2o)

        r3g,r3o,j3g,j3o=self.rhs_and_jvp(g2,o2,qg2,qo2,frozen)
        gn=(g+2*(g2+dt*r3g))/3; on=(o+2*(o2+dt*r3o))/3
        qgn=(qg+2*(qg2+dt*j3g))/3; qon=(qo+2*(qo2+dt*j3o))/3
        return gn,on,qgn,qon

    def ssprk3_step(self,g,o,dt,frozen):
        z=np.zeros_like(g)
        gn,on,_,_=self.ssprk3_step_and_jvp(g,o,z,z,dt,frozen)
        return gn,on

def hou_initial(r,z):
    R,Z=np.meshgrid(r,z,indexing="ij")
    U=12000*(1-R**2)**18*np.sin(2*np.pi*Z)/(1+12.5*np.sin(np.pi*Z)**2)
    return R**2*U, np.zeros_like(U)
