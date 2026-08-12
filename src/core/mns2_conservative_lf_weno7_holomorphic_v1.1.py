"""
Conservative LF-WENO7 holomorphic transport core — v1.1.
Enforces H_r(r=0)=H_r(r=1)=0 on the numerical flux itself.
"""
import numpy as np
import importlib.util, sys
from pathlib import Path
_P=Path(__file__).with_name('mns2_conservative_lf_weno7_holomorphic_v1.0.py')
_s=importlib.util.spec_from_file_location('_mns2_v10',_P); v10=importlib.util.module_from_spec(_s); sys.modules[_s.name]=v10; _s.loader.exec_module(v10)
frozen_eps=v10.frozen_eps; corner_fluxes=v10.corner_fluxes; discrete_div_q=v10.discrete_div_q; alpha_envelope_real=v10.alpha_envelope_real; alpha_gate_real=v10.alpha_gate_real; reflected_lr_faces_and_jvp=v10.reflected_lr_faces_and_jvp; periodic_lr_faces_and_jvp=v10.periodic_lr_faces_and_jvp

def rhs_and_jvp(f,Phi,df,dPhi,r,dr,dz,alpha_r,alpha_z,eps_abs,radial_lp=1,radial_rp=-1):
    f=np.asarray(f); Phi=np.asarray(Phi); df=np.asarray(df); dPhi=np.asarray(dPhi); nr,nz=f.shape; qr,qz=corner_fluxes(Phi,dr,dz); dqr,dqz=corner_fluxes(dPhi,dr,dz); dtype=np.result_type(f,Phi,df,dPhi)
    Lr=np.empty((nr+1,nz),dtype=dtype); Rr=np.empty_like(Lr); dLr=np.empty_like(Lr); dRr=np.empty_like(Lr)
    for j in range(nz): Lr[:,j],Rr[:,j],dLr[:,j],dRr[:,j]=reflected_lr_faces_and_jvp(f[:,j],df[:,j],radial_lp,radial_rp,eps_abs)
    rf=np.arange(nr+1)*dr; Hr=.5*(qr*(Lr+Rr)-alpha_r*rf[:,None]*(Rr-Lr)); dHr=.5*(dqr*(Lr+Rr)+qr*(dLr+dRr)-alpha_r*rf[:,None]*(dRr-dLr)); Hr[0,:]=0; Hr[-1,:]=0; dHr[0,:]=0; dHr[-1,:]=0
    Lz=np.empty((nr,nz),dtype=dtype); Rz=np.empty_like(Lz); dLz=np.empty_like(Lz); dRz=np.empty_like(Lz)
    for i in range(nr): Lz[i],Rz[i],dLz[i],dRz[i]=periodic_lr_faces_and_jvp(f[i],df[i],eps_abs)
    Hz=.5*(qz*(Lz+Rz)-alpha_z*r[:,None]*(Rz-Lz)); dHz=.5*(dqz*(Lz+Rz)+qz*(dLz+dRz)-alpha_z*r[:,None]*(dRz-dLz))
    div=(Hr[1:]-Hr[:-1])/dr+(np.roll(Hz,-1,axis=1)-Hz)/dz; ddiv=(dHr[1:]-dHr[:-1])/dr+(np.roll(dHz,-1,axis=1)-dHz)/dz
    return -div/r[:,None],-ddiv/r[:,None]

def rhs(f,Phi,r,dr,dz,alpha_r,alpha_z,eps_abs,radial_lp=1,radial_rp=-1):
    out,_=rhs_and_jvp(f,Phi,np.zeros_like(f),np.zeros_like(Phi),r,dr,dz,alpha_r,alpha_z,eps_abs,radial_lp,radial_rp); return out

def weighted_mass_rate(rhs_value,r,dr,dz): return np.sum(r[:,None]*rhs_value)*dr*dz
