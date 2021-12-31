#!python3
from calculation import *

position = [0,0]

try:
	angle = int(input("Angle : "))
	width = int(input("Width : "))
	height = int(input("Height : "))
	position[0] = int(input("x : "))
	position[1] = int(input("y : "))
	print()
except:
	print()
	print("You need to type only integer !")
else:
	end_position = [0, 0]
	try:
		end_position = calc(position, width, height, angle)
	except ValueError as error:
		if (str(error) == "angle"):
			print("Error, angle need to be beetween 0 and 360 !")
		elif (str(error) == "plan"):
			print("Error, plan width and height needs to be higher than 0 !")
		elif(str(error) == "position"):
			print("Error, position[x, y] need to be higher than 0 and lower or equal to respectively width and height !")
	else:
		print("plane size :", width,"px *", height,"px (width * height)")
		print("angle :", angle)
		print("start position : x" + str(position[0]) + " y" + str(position[1]))
		print("end position : x" + str(end_position[0]) + " y" + str(end_position[1]))
