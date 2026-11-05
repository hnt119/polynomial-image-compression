import json,sys
from itertools import combinations
from ardc_a3_exact_certificate import K
from ardc_a3_squareclass_certificate import key,unpack,inverse
exec(open('output/tcrc_m3_cover_search.py').read().split('slopes=')[0])
z=json.load(open('output/tcrc_m3_affine_exact_results.json'))
records={x['mask']:x for x in z['hit_masks']}
masks=list(set(records)|{sum(1<<x for x in ij)for ij in combinations(range(17),2)})
masks=[m for m in masks if not any(m!=n and m|n==n for n in masks)]
full=(1<<17)-1;seen={0:None};front={0};maxs=[]
for c in range(1,8):
 nf=set()
 for u in front:
  for v in masks:
   w=u|v
   if w not in seen:seen[w]=(u,v);nf.add(w)
 maxs.append(max(map(int.bit_count,nf)))
 if full in nf:break
 front=nf
cover=[];cur=full
while cur:
 old,mask=seen[cur];cover.append(mask);cur=old
print('MIN',c,'max levels',maxs,'masks',cover)
z['minimum_affine_copies']=c;z['maximum_union_by_copy_count']=maxs;z['five_cover_masks']=cover
import pickle
with open('output/tcrc_m3_exact_full_data.pkl','rb')as f: SS,RR,rich,exacts=pickle.load(f)
assert [key(x)for x in Ss]==[key(x)for x in SS]
assert [key(x)for x in Rs]==[key(x)for x in RR]
def mask_original(a,b):return sum(1<<i for i,r in enumerate(Rs)if any(a*s+b==r for s in Ss))
newexact={}
for mask,data in exacts.items():
 line=rich[data[0]][0]
 a=data[6]*unpack(inverse(line[0],6));b=data[7]-a*unpack(line[1])
 assert mask_original(a,b)==mask
 newexact[mask]=(a,b)
for mask in cover:
 if mask in newexact:a,b=newexact[mask]
 else:
  ii=[i for i in range(17)if mask>>i&1];assert len(ii)==2
  a=(Rs[ii[1]]-Rs[ii[0]])/2;b=Rs[ii[0]]-a
 assert mask_original(a,b)==mask
 print(a.text(),' ; ',b.text(),'size',mask.bit_count())
 z.setdefault('five_cover_maps',[]).append({'a':a.text(),'b':b.text(),'mask':mask})
open('output/tcrc_m3_affine_exact_results.json','w').write(json.dumps(z,indent=2))
