# get metadata from a gpkg file 

import fiona

gpkg_file_path = 'path/to/input/file/nation.gpkg'

with fiona.open(gpkg_file_path) as src:
    schema = src.schema
    print("Column Names and Data Types:")
    for field in schema['properties']:
        col_name = field
        col_data_type = schema['properties'][field]
        print(f"{col_name}: {col_data_type}")

print('Column names and data types extracted.')
