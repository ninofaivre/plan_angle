import math

def	exit_plan_position(position, width, height):
	position[0] = round(position[0])
	position[1] = round(position[1])
	if (position[0] > width):
		position[0] = width
	if (position[1] > height):
		position[1] = height
	if (position[0] < 0):
		position[0] = 0
	if (position[1] < 0):
		position[1] = 0
	return (position)

def	calc(position, width, height, angle):
	new_position = [0, 0]
	if (width < 0 or height < 0):
		raise ValueError("plan")
	if (position[0] < 0 or position[1] < 0 or position[0] > width or position[1] > height):
		raise ValueError("position")
	if (angle == 360):
		angle = 0
	if (angle >= 0 and angle <= 90):
		new_position[1] = position[1] + ((width - position[0]) * math.tan(math.radians(angle)))
		new_position[0] = position[0] + ((height - position[1]) * math.tan(math.radians(90 - angle)))
	elif (angle > 90 and angle <= 180):
		new_position[1] = position[1] + (position[0] * math.tan(math.radians(180 - angle)))
		new_position[0] = position[0] - ((height - position[1]) * math.tan(math.radians(angle - 90)))
	elif (angle > 180 and angle <= 270):
		new_position[1] = position[1] - (position[0] * math.tan(math.radians(angle - 180)))
		new_position[0] = position[0] - (position[1] * math.tan(math.radians(270 - angle)))
	elif (angle > 270 and angle <= 360):
		new_position[1] = position[1] - ((width - position[0]) * math.tan(math.radians(360 - angle)))
		new_position[0] = position[0] + (position[1] * math.tan(math.radians(angle - 270)))
	else:
		raise ValueError("angle")
	new_position = exit_plan_position(new_position, width, height)
	return (new_position)