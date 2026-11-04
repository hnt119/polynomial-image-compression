from tcrc_history_parameters import A, K, r2, sq, key
for cname,C in [('2sqrt2',2*r2),('4',K(4))]:
 cs=[]
 for name,a in A:
  for inds in cs:
   if sq((C+a)*(C+inds[0][1])) is not None:
    inds.append((name,a));break
  else:cs.append([(name,a)])
 W=set();counts=[]
 for inds in cs:
  vals=set()
  for i,(n,a) in enumerate(inds):
   for n2,b in inds[i:]:
    root=sq((C+a)*(C+b));assert root is not None
    vals.update([key(2*C+a+b+root),key(2*C+a+b-root)])
  counts.append(len(vals));W|=vals
 outside=256-sum(len(z)**2 for z in cs)
 print('LEDGER',cname,'classes',[[n for n,a in z] for z in cs],'classoutputs',counts,'withinunion',len(W),'outside',outside,'image',outside+len(W),flush=True)
