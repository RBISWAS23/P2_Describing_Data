# Import the arcpy library for working with ArcGIS geospatial data
import arcpy
import os

# Path to the File GDB
File_location = r"D:\1_BVIEER\3rd_sem\Programming for GIS- III Mr. Ronit Jadhav\Practical_2\P2_Describing_Data\P2_Describing_Data\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb"

# Feature name inside GDB
majorAttraction_fc_name = "MajorAttractions"
freeWays_fc_name = "Freeways"

# Join paths to create the full path to the feature class
majorAttrac_fc_full_path = os.path.join(File_location, majorAttraction_fc_name)
freeways_full_path =os.path.join(File_location,freeWays_fc_name)

# Use arcpy.Describe() to get information about the major attractions feature class
majorAttraction_desc_obj = arcpy.Describe(majorAttrac_fc_full_path)
freeWays_desc_obj = arcpy.Describe(freeways_full_path)

# Print the shape type of the feature class
print("The type of shape is {}".format(majorAttraction_desc_obj.shapeType))
print("The type of shape is {}".format(freeWays_desc_obj.shapeType))
print("Process Is Completed 😒")

