from ardc_a3_squareclass_standalone import *
alpha=K({32:1});r2=K({1:1});r3=K({2:1});r5=K({4:1});r7=K({8:1});r13=K({16:1})
beta=r13*(4-r3)*alpha/13
g=(K({9:1})+r2)/2;h=(K({9:1})-r2)/2
P=[('1',K(1)),('sqrt3',r3),('sqrt5',r5),('sqrt7',r7),('alpha',alpha),('beta',beta),('g',g),('h',h)]
A=[(s+n, a if s=='+' else -a) for n,a in P for s in ('+','-')]
for cname,C in [('2sqrt2',2*r2),('3',K(3)),('4',K(4)),('sqrt13',r13),('sqrt14',K({9:1})),('sqrt15',K({6:1})),('2sqrt3',2*r3),('sqrt21',K({10:1}))]:
 cs=[]
 for name,a in A:
  z=C+a
  for rep,inds in cs:
   rt=sq(z*rep)
   if rt is not None:
    inds.append(name);break
  else:cs.append([z,[name]])
 print(cname,[v for z,v in cs],flush=True)
