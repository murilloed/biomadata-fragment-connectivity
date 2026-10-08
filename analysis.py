"""Distance graph and minimum spanning forest; not an ecological suitability model."""
import math

def connectivity(fragments,max_gap):
    if not math.isfinite(max_gap) or max_gap<0:raise ValueError('Finite nonnegative gap required')
    if any(f.is_empty or not f.is_valid for f in fragments):raise ValueError('Invalid fragment')
    parent=list(range(len(fragments)))
    def find(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    edges=[]
    for i,a in enumerate(fragments):
        for j in range(i+1,len(fragments)):
            d=a.distance(fragments[j])
            if d<=max_gap:edges.append((d,i,j))
    selected=[]
    for d,i,j in sorted(edges):
        u,v=find(i),find(j)
        if u!=v:parent[u]=v;selected.append({'from':i,'to':j,'gap_m':d})
    groups={}
    for i in range(len(fragments)):groups.setdefault(find(i),[]).append(i)
    return {'fragments':len(fragments),'candidate_connections':len(edges),'components':list(groups.values()),'component_count':len(groups),'minimum_spanning_forest':selected,'total_gap_m':sum(e['gap_m'] for e in selected)}
