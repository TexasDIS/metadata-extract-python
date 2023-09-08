# Convert shape or gdbtable files to well known text 

import geopandas as gpd
import fiona

# Specify the path to the File Geodatabase
gdbtable = 'path/to/input/file/{filename}.gdbtable'

# Use fiona to list the available layers in the File Geodatabase
layers = fiona.listlayers(gdbtable)

# Iterate through the list of layers
for layername in layers:

    geodata = gpd.read_file(gdbtable, driver='FileGDBTable', layer=layername, ignore_geometry=True)
    output_wkt_path = f'path/to/output/file/{filename}.wkt'
    
    geodata.to_wkt(output_wkt_path)
    print(f'Layer "{layername}" exported to WKT.')

print('Conversion complete.')

