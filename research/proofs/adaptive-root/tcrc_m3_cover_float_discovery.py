exec(open('output/tcrc_m3_cover_search.py').read().split('slopes=')[0])
import numpy as np
from itertools import combinations
from time import time
def fl(x): lo,hi=x.iv();return float((lo+hi)/2)
Ss=sorted(Ss,key=fl);Rs=sorted(Rs,key=fl);sv=np.array(list(map(fl,Ss)));rv=np.array(list(map(fl,Rs)))
isrc,jsrc=np.array(list(combinations(range(len(Ss)),2))).T
ds=sv[jsrc]-sv[isrc]
found={};started=time()
for ri,rj in combinations(range(len(Rs)),2):
 for sign in (-1,1):
  slopes=sign*(rv[rj]-rv[ri])/ds
  shifts=(rv[ri] if sign==1 else rv[rj])-slopes*sv[isrc]
  vv=slopes[:,None]*sv+shifts[:,None]
  idx=np.searchsorted(rv,vv);idx=np.clip(idx,0,16)
  idx2=np.maximum(0,idx-1)
  near=np.where(np.abs(rv[idx]-vv)<np.abs(rv[idx2]-vv),idx,idx2)
  hit=np.abs(rv[near]-vv)<1e-9
  count=hit.sum(axis=1)
  for row in np.where(count>=3)[0]:
   mask=sum(1<<int(i) for i in set(near[row,hit[row]]))
   found.setdefault(mask,(ri,rj,sign,int(isrc[row]),int(jsrc[row])))
print('candidate masks',len(found),'elapsed',time()-started,flush=True)
exact={}
for ix,(mask,(ri,rj,sign,si,sj))in enumerate(found.items()):
 a=sign*(Rs[rj]-Rs[ri])*unpack(inverse(key(Ss[sj]-Ss[si]),6))
 b=(Rs[ri] if sign==1 else Rs[rj])-a*Ss[si]
 actual=0
 im={key(a*s+b)for s in Ss}
 for i,r in enumerate(Rs):
  if key(r)in im:actual|=1<<i
 if actual.bit_count()>=3:exact.setdefault(actual,(a,b))
 if ix%100==0:print('verified',ix,flush=True)
cs=sorted(exact,key=int.bit_count,reverse=True);full=(1<<17)-1
print('exact maps',len(cs),'best',[(x.bit_count(),exact[x][0].text(),exact[x][1].text())for x in cs[:15]],flush=True)
ans=None
for i,m in enumerate(cs):
 for j,n in enumerate(cs[i:],i):
  mn=m|n
  if mn==full:ans=[m,n];break
  if mn.bit_count()+cs[0].bit_count()<17:continue
  ans=next(([m,n,l] for l in cs if mn|l==full),None)
  if ans:break
 if ans:break
print('COVER',bool(ans))
if ans:
 for mask in ans:
  a,b=exact[mask];print('map',a.text(),' ; ',b.text(),'size',mask.bit_count())
  for i,r in enumerate(Rs):
   if mask>>i&1:
    witnesses=[s for s in Ss if a*s+b==r];assert witnesses
    print(' ',r.text(),'<=',witnesses[0].text())
import pickle
with open('output/tcrc_m3_cover_exact_maps.pkl','wb')as f:pickle.dump((Ss,Rs,exact,ans),f)
