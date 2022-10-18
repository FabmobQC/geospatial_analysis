from turfpy.transformation import intersect
from turfpy.measurement import points_within_polygon
from geojson import Feature, FeatureCollection, Polygon
import json
from ipyleaflet import Map, GeoJSON


bounderies_file = open("plaza_rosemont.geojson", "r")
stationnements_file = open("signalisation_stationnement.geojson", "r")

bounderies_data = bounderies_file.read()
bounderies = json.loads(bounderies_data)

stationnements_data = stationnements_file.read()
stationnements = json.loads(stationnements_data)

stationnements_plaza = [x for x in stationnements["features"] if x['properties']['NOM_ARROND'] == 'Rosemont - La Petite-Patrie']

points = FeatureCollection(stationnements_plaza)

result = points_within_polygon(points, bounderies["features"][0]["geometry"])

output = open("panneaux_plaza.geojson", "w")

output.write(json.dumps(result, indent=4))


output.close()

print(len(result["features"]))

m = Map(center=(45.5387105,-73.6116478), zoom=13)


geo_json = GeoJSON(
    data=result,
    style={"opacity": 1, "dashArray": "9", "fillOpacity": 0.3, "weight": 1},
    hover_style={"color": "green", "dashArray": "0", "fillOpacity": 0.5},
)

m.add_layer(geo_json)
m
