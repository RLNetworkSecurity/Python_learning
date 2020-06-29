from math import ceil

#Paint parameters
paint_litre = input("How many Litres of paint per tin: ")
paint_cost = input("How much does a tin paint cost: ")

#Room parameters
wall_length = input("enter the length of the room in metres: ")
wall_width = input("enter the width of the room in metres: ")
wall_height = input ("enter the height of the room in metres: ")

#Math to establish Square footage
room_square = (((float(wall_length)*float(wall_height))*2) + ((float(wall_width)*float(wall_height))*2))

#Calculations - How much many tins & how much it will cost
output_tins = room_square / float(paint_litre)
output_cost = ceil(float(output_tins)) * float(paint_cost)

#print outputs
print("Based on 8Sqm of coverage per litre you will need", ceil(output_tins),"tins", "it will cost £",output_cost )
