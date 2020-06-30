from math import ceil

# Paint parameters
paint_litre = input("How many Litres of paint per tin: ")
paint_cost = input("How much does a tin paint cost: ")

# Room parameters
wall_length = input("enter the length of the room in metres: ")
wall_width = input("enter the width of the room in metres: ")
wall_height = input ("enter the height of the room in metres: ")

# Calculations
wall_length_float = float(wall_length)
wall_height_float = float(wall_height)
wall_width_float = float(wall_width)
paint_litre_float = float(paint_litre)
paint_cost_float = float(paint_cost)
room_square = (((wall_length_float*wall_height_float)*2) + ((wall_width_float*wall_height_float)*2))
paint_litre_squared = 8
tins_float = room_square / (paint_litre_float * paint_litre_squared)
output_tins = int(ceil(tins_float))
output_cost = ceil(float(output_tins)) * float(paint_cost)

# Print outputs
print("Based on 8Sqm of coverage per litre you will need", output_tins,"tins", "it will cost £",output_cost)
