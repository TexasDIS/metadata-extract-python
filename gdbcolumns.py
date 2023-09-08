# Get all the metadata columns with data types from the gdb file

import fiona

gdbtable_path = 'path/to/input/file/{filename}.gdb'  

with fiona.open(gdbtable_path) as src:
    schema = src.schema
    print("Column Names and Data Types:")
    for field in schema['properties']:
        col_name = field
        col_data_type = schema['properties'][field]
        print(f"{col_name}: {col_data_type}")

print('Column names and data types extracted.')
