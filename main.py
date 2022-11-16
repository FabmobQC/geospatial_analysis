from turfpy.transformation import intersect
from turfpy.measurement import points_within_polygon
from geojson import Feature, FeatureCollection, Polygon
import json
from ipyleaflet import Map, GeoJSON
import argparse
import sys


# m = Map(center=(45.5387105,-73.6116478), zoom=13)


# geo_json = GeoJSON(
#     data=result,
#     style={"opacity": 1, "dashArray": "9", "fillOpacity": 0.3, "weight": 1},
#     hover_style={"color": "green", "dashArray": "0", "fillOpacity": 0.5},
# )

# m.add_layer(geo_json)
# m


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--signalec", help="Path to Signalec data file from Montreal Open data", required=True)
    parser.add_argument("-b", "--bounderies", help="Path to bounderies polygon file", required=True)
    parser.add_argument("-o", "--output", help="Path to output geojson file", required=True)
    parser.add_argument("-f", "--arrondissement", help="Filter input Data by arrondissement", required=False)

    args = parser.parse_args()

    if args.signalec and args.bounderies:

        bounderies_file = open(args.bounderies, "r")
        stationnements_file = open(args.signalec, "r")

        bounderies_data = bounderies_file.read()
        bounderies = json.loads(bounderies_data)

        stationnements_data = stationnements_file.read()
        stationnements = json.loads(stationnements_data)

        stationnements_filtered = stationnements

        if args.arrondissement:
            stationnements_filtered = [x for x in stationnements["features"] if x['properties']['NOM_ARROND'] == args.arrondissement]

        points = FeatureCollection(stationnements_filtered)

        result = points_within_polygon(points, bounderies["features"][0]["geometry"])

        output = open(args.output, "w")

        output.write(json.dumps(result, indent=4))

        output.close()

        print(len(result["features"]))

if __name__ == '__main__':
    sys.exit(main())    