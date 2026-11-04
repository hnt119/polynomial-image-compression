exec(open('output/tcrc_m3_cover_search.py').read().split('slopes=')[0])
from itertools import combinations
from time import time
Ebits=5
def component(x,base):return K({m&Ebits:v for m,v in x.v.items()if m&~Ebits==base})
lines={};started=time()
for i,j in combinations(range(len(Ss)),2):
 d=Ss[j]-Ss[i];lead=min(m&~Ebits for m in d.v)
 c=component(d,lead);di=d*unpack(inverse(key(c),6))
 intercept=Ss[i]-di*component(Ss[i],lead)
 lk=(key(di),key(intercept),lead)
 lines.setdefault(lk,set()).update((i,j))
# Lines from all pairs recover every line occupancy exactly.
rich=[(k,inds)for k,inds in lines.items()if len(inds)>=3]
print('rich lines',len(rich),'sizes',sorted([len(i)for _,i in rich],reverse=True),flush=True)
exact={}
for lnum,((direction,intercept,lead),indices)in enumerate(rich):
 ids=sorted(indices);coords=[component(Ss[i],lead)for i in ids]
 # The original full map is alpha=(a/direction), beta=b-alpha*intercept;
 # instead retain transformed line coordinates; output masks suffice.
 for ci,cj in combinations(range(len(coords)),2):
  deninv=unpack(inverse(key(coords[cj]-coords[ci]),6))
  for ri,rj in combinations(range(len(Rs)),2):
   for sign in (-1,1):
    a=sign*(Rs[rj]-Rs[ri])*deninv
    b=(Rs[ri]if sign==1 else Rs[rj])-a*coords[ci]
    im={key(a*x+b)for x in coords};mask=sum(1<<i for i,r in enumerate(Rs)if key(r)in im)
    if mask.bit_count()>=3:exact.setdefault(mask,(lnum,ci,cj,ri,rj,sign,a,b))
 print('line',lnum,'size',len(ids),'masks',len(exact),'elapsed',time()-started,flush=True)
cs=sorted(exact,key=int.bit_count,reverse=True);full=(1<<17)-1
ans=None;bestunion=0
# Include all two-element masks: every target pair is coverable by an affine map.
from itertools import combinations as comb
small=[sum(1<<x for x in ij)for ij in comb(range(17),2)]
allcs=cs+small
for i,m in enumerate(cs):
 for n in allcs:
  mn=m|n
  for l in allcs:
   u=mn|l
   if u.bit_count()>bestunion:bestunion=u.bit_count()
   if u==full:ans=(m,n,l);break
  if ans:break
 if ans:break
print('EXACT rich masks',len(cs),'max coverage',cs[0].bit_count(),'max three union',bestunion,'cover',ans,flush=True)
# C=4 at m3 root history B size6: U subset A3.
BB=[K(1),-K(1),r3,-r3,r7,-r7]
UU=[eps*x for x in [K(1),r3,r5,r7,alpha,beta,g,h] if key(x*x-4)in{key(b)for b in BB}for eps in(-1,1)]
RR={key(Q(x,y))for x in UU for y in UU}
print('C4 B6 U',len(UU),'R',len(RR),'RsubsetS',RR.issubset(S))
import json
with open('output/tcrc_m3_affine_exact_results.json','w')as f:json.dump({'rich_line_sizes':sorted([len(i)for _,i in rich],reverse=True),'rich_masks':len(cs),'max_map_coverage':cs[0].bit_count(),'max_three_union':bestunion,'cover_found':ans is not None,'c4_B_size':len(BB),'c4_U_size':len(UU),'c4_R_size':len(RR),'c4_R_subset_S':RR.issubset(S),'targets':[r.text()for r in Rs],'rich_lines':[{'direction':unpack(k[0]).text(),'intercept':unpack(k[1]).text(),'lead':k[2],'points':[Ss[i].text()for i in sorted(inds)],'coordinates':[component(Ss[i],k[2]).text()for i in sorted(inds)]}for k,inds in rich],'hit_masks':[{'mask':mask,'size':mask.bit_count(),'a':data[6].text(),'b':data[7].text(),'line':data[0]}for mask,data in exact.items()]},f,indent=2)

import pickle
with open('output/tcrc_m3_exact_full_data.pkl','wb')as f:pickle.dump((Ss,Rs,rich,exact),f)
