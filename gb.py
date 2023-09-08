# Convert shape or gdb files to shape files

import geopandas as gpd
import fiona
import datetime

# Path to the File Geodatabase folder
gdb_folder_path = 'path/to/input/file/{filename}.gdb'

# List available layers (feature classes) in the File Geodatabase
layers = fiona.listlayers(gdb_folder_path)

# Loop through the layers and convert to shapefiles
for layername in layers:
    # Use GeoPandas to read the feature class
    geodata = gpd.read_file(gdb_folder_path, layer=layername)

    geodata['PRE_DATE'] = geodata['PRE_DATE'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y %H:%M:%S.%f'))
    geodata['EFF_DATE'] = geodata['EFF_DATE'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y %H:%M:%S.%f'))
    
    # Filter out datetime columns
    # non_datetime_columns = [col for col in geodata.columns if not geodata[col].dtype.kind == 'M']
    # geodata_filtered = geodata[non_datetime_columns]
    
    # Define the output shapefile path
    output_shapefile = f'path/to/output/file/{layername}.shp'
    
    # Write the GeoDataFrame to a shapefile
    geodata.to_file(output_shapefile)

print('Conversion complete.')






