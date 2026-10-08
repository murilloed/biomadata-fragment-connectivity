# BiomaData — Conectividade entre fragmentos de vegetação

Protótipo geoespacial independente inspirado no contexto do BiomaData. Não modifica nem integra automaticamente a aplicação original.

Grafo de proximidade entre polígonos, componentes conexas e floresta geradora mínima com Kruskal para selecionar ligações por menor distância.

## Reproduzir
```bash
python -m pip install -r requirements.txt
python demo.py
python -m unittest discover -s tests -v
```

Varie o limiar: `python demo.py --max-gap 10 --output output/gap10`.

Exporta mapa SVG, relatório JSON e GeoJSON. `analysis.py` aceita polígonos Shapely para análise de dados autorizados. A demonstração utiliza apenas dados sintéticos em coordenadas planas locais em metros. GeoJSON local não deve ser sobreposto diretamente a mapas geográficos; dados em longitude/latitude precisam de reprojeção adequada.

## Técnicas e treinamento
Python, Shapely/GEOS e grafos, distância entre bordas e algoritmo de Kruskal. Não há treinamento de IA.

## Limites
Euclidean proximity only; links do not establish viable ecological corridors. Ignores roads, species, slope, land use and ecological resistance.

## Próximas etapas
Importar camadas autorizadas, validar CRS e geometrias e conectar a um fluxo de revisão do BiomaData. Incluir raster de resistência e caminhos de menor custo, com validação ecológica.
