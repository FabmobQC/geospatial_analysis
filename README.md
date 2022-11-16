# Script pour calculer le nombre de panneaux dans la zone de Plaza Saint-Hubert

## Reférence
https://turfpy.readthedocs.io/en/latest/measurements/points_within_polygon.html


## Install environment

First create a conda environement

`conda create -n geospatial_analysis`

Then activate the environment

`conda activate geospatial_analysis`

Install dependencies using pip

`pip install -r requirements.txt`

## How to use

`python3 main.py -s signalisation_stationnement.geojson -b zone_zfe_vieux_montreal.geojson -o zone_zfe_vieux_montreal_data.geojson`

You can also filter by `NOM_ARROND` using `-f` flag followed by the exact value from the feature field ['properties']['NOM_ARROND']

Ex:
`python3 main.py -s signalisation_stationnement.geojson -b zone_zfe_vieux_montreal.geojson -o zone_zfe_vieux_montreal_data.geojson -f 'Rosemont - La Petite-Patrie'`