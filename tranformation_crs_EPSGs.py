# CRS transformation
## This script provides a tool of transformation of X,Y coordinates between different CRS.
## Basic input is the epsg code, as well as below included libraries.
## Compiled by A.Androvitsanea (androvitsanea@archaeoengineering.org)

# Import basic libraries
from pyproj import Transformer
import pandas as pd


# Define the tranformation setting

input_crs = input("Type the four-digit code of your current crs:")

output_crs = input("Type the four-digit code of the crs you want your coordinates to be tranformed:")

# Print the given crs
print("The current crs is:", input_crs)
print("The wished crs is:", output_crs)

# One point or a whole dataset condition

condition = raw_input('Do you have one point to transform?')

if condition == 'yes':
    # Write the X and Y coordinates to be transformed
    input_x = input("Give the X coordinate:")
    input_y = input("Give the Y coordinate:")

    # Build tool for tranformation of coordinates

    transformer = Transformer.from_crs("epsg:%s" % input_crs, "epsg:%s" % output_crs)

    # Print the result

    print("These are the tranformed coordinates (X, Y):", transformer.transform(input_x, input_y))

else:
    print("Prepare your dataset the coordinates of points you want to transform in csv format, where the first column is called X and the second Y. The separator should be a semicolon (;) and the decimal a point.")
    path_date = raw_input("Give the path of your dataset: ")
    
    # Read dataset
    df = pd.read_csv(path_date, sep = ";",header = 0, decimal = ".")
   
    # Build tool for tranformation of coordinates

    transformer = Transformer.from_crs("epsg:%s" % input_crs, "epsg:%s" % output_crs)
   
    # Define the function that works row-wise performing the transformation for each set of X,Y

    def tranformation(row):
        return transformer.transform(row["X"],row["Y"])
    
    # Use the apply function of pandas to implement the above defined function to a dataset

    tranformed_dataset = df.apply(tranformation, axis=1)
    
    # Store tranformed coordinates in a csv file

    tranformed_dataset.to_csv('tranformed_dataset.csv', header=True)
  


