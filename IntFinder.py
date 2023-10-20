#-------------------------------------------------------------------------------
# Author:      MohammadalizadehkorM
#
# Created:     20/10/2023
# Copyright:   (c) MohammadalizadehkorM 2023
# Licence:     <MIT licence>
#-------------------------------------------------------------------------------

import geopandas as gpd
from shapely.geometry import Point

# Load the shapefile into a GeoDataFrame
shapefile_path = r'C:\Users\MohammadalizadehkorM\Desktop\CTN\CTN.shp'
streets_gdf = gpd.read_file(shapefile_path )

# Ask the user for the target street name or geometry
search_by = input("Search by name (N) or geometry (G)? ").upper()

if search_by == 'N':
    target_street_name = input("Enter the name of the target street: ")
    target_street = streets_gdf[streets_gdf['STREET_NAM'] == target_street_name]
elif search_by == 'G':
    x = float(input("Enter the X coordinate for the target street: "))
    y = float(input("Enter the Y coordinate for the target street: "))
    target_geometry = Point(x, y)
    target_street = streets_gdf[streets_gdf.intersects(target_geometry)]
else:
    print("Invalid input. Please enter 'N' for name or 'G' for geometry.")
    exit()

# Find streets that intersect with the target street
intersecting_streets = streets_gdf[streets_gdf.intersects(target_street.unary_union)]

# You can now access the names or geometries of intersecting streets
intersecting_street_names = intersecting_streets['STREET_NAM']
intersecting_street_geometries = intersecting_streets['geometry']

# Print the results
print("Streets that intersect with the target street:")
print(intersecting_street_names)


