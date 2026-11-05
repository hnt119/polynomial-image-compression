from ardc_a3_exact_certificate import K,F
from ardc_a3_squareclass_certificate import key,unpack,inverse
from itertools import product,combinations_with_replacement
from collections import defaultdict
r2=K({1:1});r3=K({2:1});r5=K({4:1});r7=K({8:1});r13=K({16:1});alpha=K({32:1});beta=r13*(4-r3)*alpha/13;g=(K({9:1})+r2)/2;h=(K({9:1})-r2)/2
P=[K(1),r3,r5,r7,alpha,beta,g,h];A=[eps*a for a in P for eps in (-1,1)]
def Q(x,y):return x*x+x*y+y*y
S={key(Q(x,y)): (x,y) for x in A for y in A};Ss=list(map(unpack,S))
U=[K(2),r2,(K({5:1})+r2)/2,(K({5:1})-r2)/2];U=[eps*u for u in U for eps in(-1,1)]
R={key(Q(x,y)) for x in U for y in U};Rs=list(map(unpack,R));Rindex={x:i for i,x in enumerate(R)}
print('S',len(S),'R',len(R),'S in E',sum(not(set(x.v)-{0,1,4,5})for x in Ss))
slopes={F(i,j) for i in range(-12,13)if i for j in range(1,13)}
allmaps={}
for a in slopes:
 shifts=defaultdict(set)
 for s in Ss:
  for r in Rs:shifts[key(r-a*s)].add(Rindex[key(r)])
 for b,inds in shifts.items():
  mask=sum(1<<i for i in inds)
  if len(inds)>=2:allmaps.setdefault(mask,(K(a),unpack(b)))
cs=sorted(allmaps,key=int.bit_count,reverse=True);full=(1<<17)-1
print('maps',len(cs),'best',[(x.bit_count(),allmaps[x][0].text(),allmaps[x][1].text())for x in cs[:12]])
ans=None
for i,m in enumerate(cs):
 for j,n in enumerate(cs[i:],i):
  mn=m|n
  if mn==full:ans=[m,n];break
  if mn.bit_count()+cs[0].bit_count()<17:continue
  ans=next(([m,n,l] for l in cs if mn|l==full),None)
  if ans:break
 if ans:break
if ans:
 print('COVER')
 for mask in ans:
  a,b=allmaps[mask];print(a.text(),b.text(),mask.bit_count())
  for i,r in enumerate(Rs):
   if mask>>i&1:
    witnesses=[s for s in Ss if a*s+b==r];assert witnesses
    print(' ',r.text(),'<=',witnesses[0].text())
else:print('NO 3 COVER in rational slopes')
