# Extract all the metadata with values from a gdb file

import fiona

# Define the path to the Geodatabase table
gdbtable_path = 'path/to/input/file/{filename}.gdb'

# Define the path to the output text file
output_file_path = 'path/to/output/file/{filename}.txt'

# Open the output text file in write mode
with open(output_file_path, 'w') as output_file:
    # Open the Geodatabase table using fiona
    with fiona.open(gdbtable_path) as src:
        # Iterate through each feature in the dataset
        for feature in src:
            # Write a header for each feature
            output_file.write(f"Feature ID: {feature['id']}\n")
            
            # Iterate through the properties (columns) in the feature's attributes
            for col_name, col_value in feature['properties'].items():
                # Write the column name and its corresponding value to the file
                output_file.write(f"{col_name}: {col_value}\n")
            
            # Write a separator between features
            output_file.write("=" * 30 + "\n")

# Print a message indicating the extraction is complete
print('Column values extracted and saved to', output_file_path)

