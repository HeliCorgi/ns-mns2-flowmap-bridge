import numpy as np

B7=np.array([
[[547,-1941,2321,-927],[-1941,7043,-8623,3521],[2321,-8623,11003,-4701],[-927,3521,-4701,2107]],
[[267,-821,801,-247],[-821,2843,-2983,961],[801,-2983,3443,-1261],[-247,961,-1261,547]],
[[547,-1261,961,-247],[-1261,3443,-2983,801],[961,-2983,2843,-821],[-247,801,-821,267]],
[[2107,-4701,3521,-927],[-4701,11003,-8623,2321],[3521,-8623,7043,-1941],[-927,2321,-1941,547]],
],dtype=float)/240.0
Q7=np.array([[-1/4,13/12,-23/12,25/12],[1/12,-5/12,13/12,1/4],[-1/12,7/12,7/12,-1/12],[1/4,13/12,-5/12,1/12]],dtype=float)
D7=np.array([1/35,12/35,18/35,4/35],dtype=float)

def frozen_eps(scale_ref,eps0=1e-6): return float(eps0)*max(1.0,float(scale_ref)**2)

def _pad(f,lp=1,rp=1,ng=4):
    f=np.asarray(f); left=np.array([lp*f[k] for k in range(ng-1,-1,-1)]); right=np.array([rp*f[-1-k] for k in range(ng)])
    return np.concatenate([left,f,right])

def _faces(vals,dvals,eps_abs):
    q=np.einsum('fki,ki->fk',vals,Q7); dq=np.einsum('fki,ki->fk',dvals,Q7)
    beta=np.einsum('fki,kij,fkj->fk',vals,B7,vals); dbeta=2*np.einsum('fki,kij,fkj->fk',dvals,B7,vals)
    den=beta+eps_abs; alpha=D7[None,:]/den**2; dalpha=-2*alpha*dbeta/den
    asum=np.sum(alpha,axis=1,keepdims=True); dasum=np.sum(dalpha,axis=1,keepdims=True)
    w=alpha/asum; dw=(dalpha*asum-alpha*dasum)/(asum**2)
    return np.sum(w*q,axis=1), np.sum(dw*q+w*dq,axis=1)

def reflected_left_faces_and_jvp(f,df,lp=1,rp=1,eps_abs=1e-6):
    f=np.asarray(f); df=np.asarray(df); a=_pad(f,lp,rp,4); da=_pad(df,lp,rp,4); n=f.size; i=np.arange(n+1); j=i-1; p=j+4
    ids=[np.stack([p-3,p-2,p-1,p],axis=-1),np.stack([p-2,p-1,p,p+1],axis=-1),np.stack([p-1,p,p+1,p+2],axis=-1),np.stack([p,p+1,p+2,p+3],axis=-1)]
    vals=np.stack([a[ii] for ii in ids],axis=1); dvals=np.stack([da[ii] for ii in ids],axis=1)
    return _faces(vals,dvals,eps_abs)

def reflected_lr_faces_and_jvp(f,df,lp=1,rp=1,eps_abs=1e-6):
    L,dL=reflected_left_faces_and_jvp(f,df,lp,rp,eps_abs); Lr,dLr=reflected_left_faces_and_jvp(f[::-1],df[::-1],rp,lp,eps_abs)
    return L,Lr[::-1],dL,dLr[::-1]

def periodic_left_faces_and_jvp(f,df,eps_abs=1e-6):
    f=np.asarray(f); df=np.asarray(df); n=f.size; i=np.arange(n); j=i-1
    ids=[np.stack([(j-3)%n,(j-2)%n,(j-1)%n,j%n],axis=-1),np.stack([(j-2)%n,(j-1)%n,j%n,(j+1)%n],axis=-1),np.stack([(j-1)%n,j%n,(j+1)%n,(j+2)%n],axis=-1),np.stack([j%n,(j+1)%n,(j+2)%n,(j+3)%n],axis=-1)]
    vals=np.stack([f[ii] for ii in ids],axis=1); dvals=np.stack([df[ii] for ii in ids],axis=1)
    return _faces(vals,dvals,eps_abs)

def periodic_lr_faces_and_jvp(f,df,eps_abs=1e-6):
    L,dL=periodic_left_faces_and_jvp(f,df,eps_abs); Lr,dLr=periodic_left_faces_and_jvp(f[::-1],df[::-1],eps_abs)
    return L,np.roll(Lr[::-1],1),dL,np.roll(dLr[::-1],1)

def corner_fluxes(Phi,dr,dz):
    Phi=np.asarray(Phi); return -(np.roll(Phi,-1,axis=1)-Phi)/dz,(Phi[1:]-Phi[:-1])/dr

def discrete_div_q(qr,qz,dr,dz): return (qr[1:]-qr[:-1])/dr+(np.roll(qz,-1,axis=1)-qz)/dz

def alpha_envelope_real(Phi,r,dr,dz,safety=1.10):
    qr,qz=corner_fluxes(np.asarray(Phi,float),dr,dz); rf=np.arange(len(r)+1)*dr; ur=np.zeros_like(qr); ur[1:]=qr[1:]/rf[1:,None]; uz=qz/r[:,None]
    return safety*max(float(np.max(np.abs(ur))),1e-15),safety*max(float(np.max(np.abs(uz))),1e-15),ur,uz

def alpha_gate_real(Phi,r,dr,dz,alpha_r,alpha_z):
    _,_,ur,uz=alpha_envelope_real(Phi,r,dr,dz,1.0); um=float(np.max(np.abs(ur))); zm=float(np.max(np.abs(uz)))
    return {'ur_max':um,'uz_max':zm,'radial_margin':float(alpha_r-um),'axial_margin':float(alpha_z-zm),'pass_gate':bool(alpha_r>=um and alpha_z>=zm)}

def rhs_and_jvp(f,Phi,df,dPhi,r,dr,dz,alpha_r,alpha_z,eps_abs,radial_lp=1,radial_rp=1):
    f=np.asarray(f); Phi=np.asarray(Phi); df=np.asarray(df); dPhi=np.asarray(dPhi); nr,nz=f.shape; qr,qz=corner_fluxes(Phi,dr,dz); dqr,dqz=corner_fluxes(dPhi,dr,dz); dtype=np.result_type(f,Phi,df,dPhi)
    Lr=np.empty((nr+1,nz),dtype=dtype); Rr=np.empty_like(Lr); dLr=np.empty_like(Lr); dRr=np.empty_like(Lr)
    for j in range(nz): Lr[:,j],Rr[:,j],dLr[:,j],dRr[:,j]=reflected_lr_faces_and_jvp(f[:,j],df[:,j],radial_lp,radial_rp,eps_abs)
    rf=np.arange(nr+1)*dr; Hr=.5*(qr*(Lr+Rr)-alpha_r*rf[:,None]*(Rr-Lr)); dHr=.5*(dqr*(Lr+Rr)+qr*(dLr+dRr)-alpha_r*rf[:,None]*(dRr-dLr))
    Lz=np.empty((nr,nz),dtype=dtype); Rz=np.empty_like(Lz); dLz=np.empty_like(Lz); dRz=np.empty_like(Lz)
    for i in range(nr): Lz[i],Rz[i],dLz[i],dRz[i]=periodic_lr_faces_and_jvp(f[i],df[i],eps_abs)
    Hz=.5*(qz*(Lz+Rz)-alpha_z*r[:,None]*(Rz-Lz)); dHz=.5*(dqz*(Lz+Rz)+qz*(dLz+dRz)-alpha_z*r[:,None]*(dRz-dLz))
    div=(Hr[1:]-Hr[:-1])/dr+(np.roll(Hz,-1,axis=1)-Hz)/dz; ddiv=(dHr[1:]-dHr[:-1])/dr+(np.roll(dHz,-1,axis=1)-dHz)/dz
    return -div/r[:,None],-ddiv/r[:,None]

def rhs(f,Phi,r,dr,dz,alpha_r,alpha_z,eps_abs,radial_lp=1,radial_rp=1):
    out,_=rhs_and_jvp(f,Phi,np.zeros_like(f),np.zeros_like(Phi),r,dr,dz,alpha_r,alpha_z,eps_abs,radial_lp,radial_rp); return out
