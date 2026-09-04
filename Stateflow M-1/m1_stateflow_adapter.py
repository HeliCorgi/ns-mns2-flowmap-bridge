"""M-1 adapter following kernel-dynamics-viewer/stateflow core semantics.
Local analysis helper only; does not modify either repository.
"""
from dataclasses import dataclass, field
from typing import Any, Optional
import numpy as np, json

@dataclass
class FeatureSeries:
    time: np.ndarray
    features: np.ndarray
    feature_names: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    uncertainty: Optional[np.ndarray] = None
    mask: Optional[np.ndarray] = None
    def __post_init__(self):
        self.time=np.asarray(self.time,float); self.features=np.asarray(self.features,float)
        if self.mask is None: self.mask=np.ones(len(self.time),bool)
        else: self.mask=np.asarray(self.mask,bool)
        self.metadata.setdefault('provenance','unspecified')
    def column(self,name):
        j=self.feature_names.index(name); return self.features[:,j]

@dataclass
class Transition:
    index:int; time:float; kind:str; detail:dict[str,Any]=field(default_factory=dict)
@dataclass
class Trajectory:
    times:np.ndarray; values:Any; mask:Optional[np.ndarray]=None; transitions:list[Transition]=field(default_factory=list); name:str=''
    def __post_init__(self):
        self.times=np.asarray(self.times,float)
        if self.mask is None:self.mask=np.ones(len(self.times),bool)

class TransitionAnalyzer:
    def from_threshold(self,times,scalar,threshold):
        times=np.asarray(times,float); scalar=np.asarray(scalar,float); above=scalar>threshold; tr=[]
        for i in range(1,len(scalar)):
            if np.isfinite(scalar[i]) and np.isfinite(scalar[i-1]) and above[i]!=above[i-1]:
                tr.append(Transition(i,float(times[i]),'rise' if above[i] else 'fall'))
        out=Trajectory(times,scalar,np.isfinite(scalar),tr,'threshold'); out.above=above; return out
    def from_labels(self,times,labels):
        tr=[]; prev=None
        for i,lab in enumerate(labels):
            if lab is None: continue
            if prev is not None and lab!=prev: tr.append(Transition(i,float(times[i]),f'{prev}->{lab}'))
            prev=lab
        out=Trajectory(times,np.arange(len(times),dtype=float),transitions=tr,name='labels'); out.labels=labels; return out

def build(path):
    rows=json.load(open(path)); t=np.array([r['t'] for r in rows]);
    names=['E','Lam','C1','beta_top1','beta_int','deltaB','C4','cos2_2_int','twist_share','tail']
    X=np.array([[r[n] for n in names] for r in rows],float)
    fs=FeatureSeries(t,X,names,metadata={'provenance':'GPT rerun of repo experiments/m1_events E0 solver conventions; stateflow-style adapter','run':'E0','N':64,'nu':0.02})
    E=fs.column('E'); Ep=np.gradient(E,t); db=fs.column('deltaB'); btop=fs.column('beta_top1'); bint=fs.column('beta_int'); c4=fs.column('C4')
    nested=np.where((btop<0.5)&(bint>0.5),'NESTED_FLUX_CORE_SOURCE_OUTER','OTHER').tolist()
    shield=np.where(c4<0.5,'PRESSURE_SHIELDED','PRESSURE_SURVIVES').tolist()
    growth=np.where(Ep>0,'ENSTROPHY_GROWTH','NO_GROWTH').tolist()
    ta=TransitionAnalyzer(); nt=ta.from_labels(t,nested); pt=ta.from_labels(t,shield); gt=ta.from_labels(t,growth)
    return fs,Ep,nt,pt,gt

if __name__=='__main__':
    fs,Ep,nt,pt,gt=build('/mnt/data/m1_scratch/E0_stateflow_timeseries_partial.json')
    out={'time':fs.time.tolist(),'feature_names':fs.feature_names,'features':fs.features.tolist(),'Eprime':Ep.tolist(),
         'transitions':{'nested':[vars(x) for x in nt.transitions],'pressure':[vars(x) for x in pt.transitions],'growth':[vars(x) for x in gt.transitions]},
         'metadata':fs.metadata}
    json.dump(out,open('/mnt/data/m1_scratch/M1_STATEFLOW_E0_ANALYSIS.json','w'),indent=2)
    print(json.dumps(out['transitions'],indent=2))
