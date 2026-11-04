"""Exact finite nonlinear-chart audits, with full-square completion charged.

All coordinates are rational coefficients in A=hB, where h=1 or 1/sqrt(3).
The fixed cubic satisfies P(hx,hy)/h=lambda*(x-y)^3+x+y, lambda=h^2.
No historical grid or symmetry-graph driver is invoked.
"""

from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json
import platform
import sys
import time

MAX_MODELS, MAX_INPUTS, MAX_P, MAX_CHECKS, MAX_CPU = 36, 160, 400_000, 3_000_000, 60


class Budget:
    def __init__(self):
        self.checks = Counter()
        self.start_cpu = time.process_time()

    def charge(self, category, count):
        if sum(self.checks.values())+count > MAX_CHECKS:
            raise RuntimeError("Check budget exhausted before batch")
        if category == "full_square_P_evaluations" and self.checks[category]+count > MAX_P:
            raise RuntimeError("Full-square P budget exhausted before batch")
        if time.process_time()-self.start_cpu > MAX_CPU:
            raise RuntimeError("Research CPU cap exhausted")
        self.checks[category] += count


def normalized_polynomial(x, y, lam=Q(1)):
    return lam*(x-y)**3+x+y


def coordinates(z, u, lam=Q(1)):
    return (z-lam*u**3+u)/2, (z-lam*u**3-u)/2


def conic(t):
    t = Q(t)
    denominator = 1+t+t*t
    return (1-t*t)/denominator, t*(t+2)/denominator


def nodal(t):
    t = Q(t)
    if t == 1:
        raise ValueError("The nodal rational chart excludes t=1")
    a = 3*(1+t*t)/(1-t**3)
    return 1-a, -1-t*a


def model(identifier, family, labels, lam=Q(1), parameters=None, scope="", stop=""):
    values = tuple(sorted({a for x,y,_,_ in labels for a in (x,y)}))
    return {"id":identifier,"family":family,"labels":labels,"lambda":lam,
            "values":values,"parameters":parameters or {},"scope":scope,"stop":stop}


def augmented(base, kind):
    labels = list(base["labels"])
    if kind == "transpose_diagonal":
        labels += [(y,x,["transpose",i],None) for i,(x,y,_,_) in enumerate(base["labels"])]
        labels += [(x,x,["diagonal",i],None) for i,x in enumerate(base["values"])]
    elif kind == "full_completion":
        old = {(x,y) for x,y,_,_ in labels}
        labels += [(x,y,["complement",i,j],None) for i,x in enumerate(base["values"]) for j,y in enumerate(base["values"]) if (x,y) not in old]
    else:
        raise ValueError(kind)
    return model(base["id"]+"_"+kind, base["family"]+"_"+kind, labels, base["lambda"],
                 {**base["parameters"],"completion":kind},base["scope"],
                 "Completion audit on this same fixed scalar carrier only; no size expansion and no success claim from automatic Cartesian completion.")


def definitions():
    for kind in ("squares","rational"):
        for m in (5,9):
            f = (lambda j: Q(j*j)) if kind=="squares" else (lambda j: Q(j,j+1))
            labels = [(f(r),f((s+r*r)%m),[r,s],None) for r,s in product(range(m),repeat=2)]
            yield model(f"permuted_{kind}_m{m}","full_square_reindexing_control",labels,
                        parameters={"m":m,"f":kind,"column_index":"(s+r^2) mod m"},
                        scope="Modulo reindexing is not a bounded-degree rational chart. It preserves the full Cartesian square and all its outputs.",
                        stop="Two small reindexing controls only. Automatic full-square coordinate reuse is not a new compression mechanism.")
    for m in (3,5):
        labels=[(Q(r*r),Q(s*s),[r,s],None) for r,s in product(range(-m,m+1),repeat=2)]
        yield model(f"signed_square_m{m}","many_to_one_full_square_control",labels,
                    parameters={"m":m,"range":[-m,m]},scope="The map (r,s)->(r²,s²) has genuine parameter multiplicities, but its actual pair set is a Cartesian square.",
                    stop="Two small multiplicity controls only; repeated labels do not change selected or full output support.")
    for kind in ("quadratic_sum","product"):
        labels=[]
        for r,s in product((1,2),repeat=2):
            u=Q(r+s*s) if kind=="quadratic_sum" else Q(r*s)
            z=Q(r+s)
            x,y=coordinates(z,u)
            labels.append((x,y,[r,s],z))
        yield model(f"forced_{kind}_m2","output_forced_low_degree",labels,
                    parameters={"m":2,"U":"r+s²" if kind=="quadratic_sum" else "rs","Z":"r+s","L":"Z-U³"},
                    scope="U and Z have degree at most two; L=Z-U³ can have degree six. This is not a claim that both U and L are quadratic.",
                    stop="Stop after the single minimal size: compare distinct selected pairs with actual scalars and charge the uncovered square; no larger sparse chart search.")
    for family in ("conic","nodal"):
        lam=Q(1) if family=="conic" else Q(1,3)
        indices=range(-2,3) if family=="conic" else range(-2,2)
        for h in (1,2):
            labels=[]
            for b,j in product(range(h),indices):
                t=Q(j,2)
                u,v=conic(t) if family=="conic" else nodal(t)
                z=Q(2*b)
                w=z if family=="conic" else z+Q(4,3)
                x,y=coordinates(z,u,lam)
                xp,yp=coordinates(w,v,lam)
                if x != xp:
                    raise AssertionError("Prescribed exact coordinate-sharing identity failed")
                labels.extend(((x,y,[b,j,"u"],z),(xp,yp,[b,j,"v"],w)))
            base=model(f"{family}_H{h}","same_output_conic" if family=="conic" else "distinct_output_nodal",labels,lam,
                       {"H":h,"t_indices":list(indices),"t_denominator":2,"outputs":"2b" if family=="conic" else "2b and 2b+4/3 in normalized units"},
                       "The u/v matching is a nonlinear conic relation, not one fixed affine template map." if family=="conic" else "The distinct-output matching has a nonconstant nonlinear rational u/v relation; no fixed translation step is imposed.",
                       "Only the minimal H1/H2 illustrations: scalar count comparable to distinct selected-pair count triggers no further size expansion.")
            yield base
            if h==2:
                yield augmented(base,"transpose_diagonal")
                yield augmented(base,"full_completion")


def cache_key(chart):
    return chart["lambda"],chart["values"]


def preflight(charts):
    unique={cache_key(c) for c in charts}
    result={"model_records":len(charts),"distinct_normalized_carriers":len(unique),
            "maximum_N":max(len(c["values"]) for c in charts),
            "cached_full_square_P_evaluations":sum(len(values)**2 for _,values in unique),
            "formal_label_construction_checks":sum(len(c["labels"]) for c in charts),
            "models":[{"id":c["id"],"N":len(c["values"]),"Q0":len(c["labels"]),
                       "Q":len({(x,y) for x,y,_,_ in c["labels"]}),"lambda":str(c["lambda"]),"stop":c["stop"]} for c in charts]}
    if len(charts)>MAX_MODELS or result["maximum_N"]>MAX_INPUTS or result["cached_full_square_P_evaluations"]>MAX_P:
        raise RuntimeError("Declared preflight exceeds allocation")
    return result


def enumerate_carrier(chart,budget):
    values,lam=chart["values"],chart["lambda"]
    n=len(values)
    budget.charge("full_square_P_evaluations",n*n)
    fibers=defaultdict(list)
    for i,x in enumerate(values):
        for j,y in enumerate(values):
            fibers[normalized_polynomial(x,y,lam)].append(i*n+j)
    ordered=sorted(fibers.items())
    output_of_vertex=[-1]*(n*n)
    for k,(_,vertices) in enumerate(ordered):
        for v in vertices:
            output_of_vertex[v]=k
    return {"N":n,"values":values,"lambda":lam,"fibers":ordered,"output_of_vertex":output_of_vertex}


def audit_chart(chart,carrier,budget):
    n=carrier["N"]
    budget.charge("formal_chart_pair_checks",len(chart["labels"]))
    budget.charge("chart_full_square_coverage_checks",n*n)
    indices={x:i for i,x in enumerate(carrier["values"])}
    by_pair=defaultdict(list)
    projection=defaultdict(list)
    for label_index,(x,y,label,expected) in enumerate(chart["labels"]):
        vertex=indices[x]*n+indices[y]
        by_pair[vertex].append({"label_index":label_index,"parameters":label})
        projection[str(x)].append([label_index,"x"])
        projection[str(y)].append([label_index,"y"])
        z=carrier["fibers"][carrier["output_of_vertex"][vertex]][0]
        if expected is not None and z != expected:
            raise AssertionError("Chart output identity disagrees with full enumeration")
    selected=set(by_pair)
    selected_outputs={carrier["output_of_vertex"][v] for v in selected}
    outside=set(range(n*n))-selected
    outside_outputs={carrier["output_of_vertex"][v] for v in outside}
    budget.charge("fiber_overlap_checks",len(carrier["fibers"]))
    details=[]
    ss=so=oo=outside_shared_mass=0
    for z,vertices in carrier["fibers"]:
        inside=[v for v in vertices if v in selected]
        rest=[v for v in vertices if v not in selected]
        a,b=len(inside),len(rest)
        ss+=a*(a-1)//2;so+=a*b;oo+=b*(b-1)//2
        if a:
            outside_shared_mass+=b
        details.append({"output":str(z),"selected_vertices":inside,"outside_vertices":rest})
    q0,q,zcount=len(chart["labels"]),len(selected),len(selected_outputs)
    full=len(carrier["fibers"])
    if not full <= zcount+n*n-q or len(selected)+len(outside)!=n*n:
        raise AssertionError("Full-square completion inequality failed")
    sizes=[len(v) for _,v in carrier["fibers"]]
    return {"id":chart["id"],"family":chart["family"],"parameters":chart["parameters"],"scope":chart["scope"],"stop":chart["stop"],
            "normalization":{"lambda":str(chart["lambda"]),"h":"1" if chart["lambda"]==1 else "1/sqrt(3)","identity":"P(hx,hy)/h=lambda*(x-y)^3+x+y"},
            "inputs_in_units_of_h":list(map(str,carrier["values"])),"N":n,"Q0":q0,"Q":q,"selected_image_size":zcount,"full_image_size":full,
            "uncovered_pairs":n*n-q,"selected_pair_fraction":str(Q(q,n*n)),"safe_full_image_upper_bound":zcount+n*n-q,
            "formal_pair_projection_multiplicity_distribution":dict(sorted(Counter(map(len,by_pair.values())).items())),
            "maximum_formal_pair_multiplicity":max(map(len,by_pair.values())),"formal_pair_projection_fibers":dict(sorted(by_pair.items())),
            "coordinate_projection_multiplicity_distribution":dict(sorted(Counter(map(len,projection.values())).items())),
            "coordinate_projection_fibers":dict(projection),"formal_coordinate_occurrences":2*q0,"formal_coordinate_reuse":str(Q(2*q0,n)),
            "distinct_selected_coordinate_occurrences":2*q,"distinct_selected_coordinate_reuse":str(Q(2*q,n)),"distinct_pair_label_reuse":str(Q(q0,q)),
            "maximum_actual_fiber":max(sizes),"actual_fiber_size_distribution":dict(sorted(Counter(sizes).items())),"average_actual_fiber":str(Q(n*n,full)),
            "outside_output_count":len(outside_outputs),"new_outputs_outside_selected":len(outside_outputs-selected_outputs),
            "shared_selected_outside_outputs":len(outside_outputs&selected_outputs),"outside_pair_mass_in_selected_outputs":outside_shared_mass,
            "unordered_collision_counts":{"selected_selected":ss,"selected_outside":so,"outside_outside":oo},
            "selected_vertices":sorted(selected),"per_output_membership":details}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path,data):
    if path.exists():
        raise RuntimeError(f"Refusing to overwrite {path}")
    path.write_text(json.dumps(data,indent=2)+"\n")


def run(directory,portable):
    budget=Budget();wall=time.perf_counter()
    if (directory/"provenance.json").exists() or portable.exists():
        raise RuntimeError("Refusing to overwrite existing nonlinear-grid artifacts")
    charts=list(definitions()); declared=preflight(charts)
    budget.charge("formal_label_construction_checks",declared["formal_label_construction_checks"])
    directory.mkdir(parents=True,exist_ok=True)
    cache={};carriers=[];records=[];errors=[]
    try:
        for chart in charts:
            key=cache_key(chart)
            if key not in cache:
                c=enumerate_carrier(chart,budget)
                carrier_id=f"carrier{len(cache)+1:02}"
                raw={"id":carrier_id,"N":c["N"],"lambda":str(c["lambda"]),"inputs_in_units_of_h":list(map(str,c["values"])),
                     "full_fibers":[{"output_in_units_of_h":str(z),"vertices":v} for z,v in c["fibers"]],"pair_output_index":c["output_of_vertex"]}
                path=directory/(carrier_id+".json");write_new(path,raw)
                entry={"id":carrier_id,"N":c["N"],"lambda":str(c["lambda"]),"raw_path":str(path),"raw_sha256":sha(path)}
                carriers.append(entry);cache[key]=(c,entry)
            c,entry=cache[key]
            record=audit_chart(chart,c,budget);record["carrier_id"]=entry["id"]
            path=directory/(chart["id"]+".json");write_new(path,record)
            record.update(raw_path=str(path),raw_sha256=sha(path))
            records.append({k:v for k,v in record.items() if k not in {"formal_pair_projection_fibers","coordinate_projection_fibers","selected_vertices","per_output_membership"}})
    except Exception as error:
        errors.append({"type":type(error).__name__,"message":str(error),"completed_models":len(records)})
    result={"date":"2026-09-21","claim_id":"NR-X1","status":"EXPERIMENTAL exact finite chart audits","polynomial":"(x-y)^3+x+y",
            "preflight":declared,"carriers":carriers,"models":records,"errors":errors,
            "limitations":"Finite reindexing controls and complement-completion audits are not new mechanisms. Sparse reverse designs stop at the declared minimal sizes. All h=1/sqrt(3) records are exact rational normalized computations for the same fixed P."}
    write_new(portable,result)
    provenance={"date":"2026-09-21","command":"python3 -m experiments.nonlinear_reuse","python":sys.version,"implementation":platform.python_implementation(),
                "network":"none","randomness":"none","source_sha256":sha(Path(__file__)),"portable_sha256":sha(portable),"preflight":declared,
                "limits":{"models":MAX_MODELS,"N":MAX_INPUTS,"full_P_evaluations":MAX_P,"checks":MAX_CHECKS,"research_cpu_seconds":MAX_CPU},
                "actual":{"models":len(records),"distinct_normalized_carriers":len(cache),"checks_by_category":dict(budget.checks),"charged_checks":sum(budget.checks.values()),"cpu_seconds":time.process_time()-budget.start_cpu,"wall_seconds":time.perf_counter()-wall},
                "errors":errors,"inspection":"Entire new code read before execution; exact normalization, Q0/Q separation, cached full support and complement accounting inspected."}
    write_new(directory/"provenance.json",provenance)
    print(json.dumps({"actual":provenance["actual"],"errors":errors},indent=2))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preflight",action="store_true")
    parser.add_argument("--directory",type=Path,default=Path("local-only/runs/T01/2026-09-21-nonlinear-reuse"))
    parser.add_argument("--portable",type=Path,default=Path("examples/2026-09-21-nonlinear-reuse.json"))
    args=parser.parse_args()
    if args.preflight:
        start=time.process_time();result=preflight(list(definitions()));result["cpu_seconds"]=time.process_time()-start
        print(json.dumps(result,indent=2))
    else:
        run(args.directory,args.portable)


if __name__=="__main__":
    main()
