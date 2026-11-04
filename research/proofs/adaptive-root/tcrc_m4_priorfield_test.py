from ardc_a3_squareclass_standalone import *
alpha=K({32:1});r2=K({1:1});r3=K({2:1});r5=K({4:1});r7=K({8:1});r13=K({16:1})
beta=r13*(4-r3)*alpha/13;g=(K({9:1})+r2)/2;h=(K({9:1})-r2)/2
P=[('1',K(1)),('sqrt3',r3),('sqrt5',r5),('sqrt7',r7),('alpha',alpha),('beta',beta),('g',g),('h',h)]
A=[(s+n, a if s=='+' else -a) for n,a in P for s in ('+','-')]
d=3-r7; di=unpack(inverse(key(d),6));hs=[(name,(3+a)*di)for name,a in A]
cs=[]
for name,v in hs:
 for rep,inds in cs:
  if sq(v*rep) is not None:inds.append(name);break
 else:cs.append([v,[name]])
print('characters',[(names,sq(v)is not None) for v,names in cs])
for name,v in hs:
 z=16-v; rt=sq(z)
 compatible=[]
 for vv,names in cs:
  if sq(v*vv)is not None:continue
  if sq(z*vv)is not None:compatible.append(names)
 print(name,'norm_square',None if rt is None else rt.text(),'other compatible classes',compatible)
