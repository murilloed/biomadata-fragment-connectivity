import argparse,json
from pathlib import Path
from shapely.geometry import box,mapping,LineString
from shapely.ops import nearest_points
from analysis import connectivity

def drawing(polygons,connections=()):
    paths=[]
    for p,color in polygons:
        shapes=list(p.geoms) if p.geom_type=='MultiPolygon' else [p]
        for g in shapes:
            if g.is_empty:continue
            rings=[g.exterior,*g.interiors]
            d=' '.join('M '+' L '.join(f'{x},{y}' for x,y in r.coords)+' Z' for r in rings)
            paths.append(f'<path d="{d}" fill="{color}" fill-rule="evenodd" stroke="#73c4d3" stroke-width=".6"/>')
    for line in connections:
        (x,y),(xx,yy)=line.coords;paths.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="#efb66b" stroke-width="1.5"/>')
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="-5 -5 110 80"><rect x="-5" y="-5" width="110" height="80" fill="#0b1c33"/>'+''.join(paths)+'</svg>'

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='output');p.add_argument('--max-gap',type=float,default=18);a=p.parse_args();o=Path(a.output);o.mkdir(parents=True,exist_ok=True)
 fragments=[box(5,10,22,28),box(35,12,50,30),box(64,15,80,35),box(84,50,98,65)];metrics=connectivity(fragments,a.max_gap);lines=[LineString(nearest_points(fragments[e['from']],fragments[e['to']])) for e in metrics['minimum_spanning_forest']];polygons=[(f,'#247f66') for f in fragments];features=[{'type':'Feature','properties':{'kind':'fragment','id':i},'geometry':mapping(f)} for i,f in enumerate(fragments)]+[{'type':'Feature','properties':{'kind':'candidate_link','gap_m':e['gap_m']},'geometry':mapping(l)} for e,l in zip(metrics['minimum_spanning_forest'],lines)]
 report={'synthetic':True,'trained_model':False,'coordinate_system':'local planar meters; reproject geographic data before measuring','metrics':metrics,'limitation':'Euclidean proximity only; links do not establish viable ecological corridors. Ignores roads, species, slope, land use and ecological resistance.'}
 (o/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8');(o/'map.svg').write_text(drawing(polygons,lines),encoding='utf-8')
 (o/'analysis.geojson').write_text(json.dumps({'type':'FeatureCollection','features':features}),encoding='utf-8');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
