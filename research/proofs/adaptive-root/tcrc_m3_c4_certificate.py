from ardc_a3_squareclass_certificate import sq
exec(open('output/tcrc_m3_cover_search.py').read().split('slopes=')[0])
import json
classes=[]
for a in A:
 for cl in classes:
  if sq((4+a)*(4+cl[0]))is not None:cl.append(a);break
 else:classes.append([a])
inside={key(8+a+b+sg*sq((4+a)*(4+b)))for cl in classes for a,b in combinations_with_replacement(cl,2)for sg in(-1,1)}
sizes=list(map(len,classes));total=256-sum(n*n for n in sizes)+len(inside)
assert sizes==[6]+[1]*10 and len(inside)==61 and total==271
with open('output/tcrc_m3_c4_results.json','w')as f:json.dump({'class_sizes':sizes,'classes':[[x.text()for x in cl]for cl in classes],'inside_count':len(inside),'total_count':total},f,indent=2)
print('C4',sizes,len(inside),total)
