import math

day_inputs = open('input.txt', 'r')
inputs_list = day_inputs.readlines()
instructions_data = []

for i in inputs_list:
    if i != "\n":
        instruction = [i[0], int(i[1:len(i)-1])]
        instructions_data.append(instruction)

x_delta = 0
y_delta = 0
orientation_degrees = 0

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.

for instruction in instructions_data:
    action = instruction[0]
    value = instruction[1]

    if action == 'N':
        y_delta += value
    if action == 'S':
        y_delta -= value
    if action == 'E':
        x_delta += value
    if action == 'W':
        x_delta -= value
    if action == 'L':
        orientation_degrees -= value
    if action == 'R':
        orientation_degrees += value
    if action == 'F':
        if abs(orientation_degrees) % 360 == 0: # E
            x_delta += value
        if orientation_degrees % 360 == 90 or orientation_degrees % 360 == -270: # S
            y_delta -= value
        if abs(orientation_degrees) % 360 == 180: # W
            x_delta -= value
        if orientation_degrees % 360 == 270 or orientation_degrees % 360 == -90: # N
            y_delta += value

manhattan_distance = abs(x_delta) + abs(y_delta)
print(manhattan_distance)

day_inputs.close()

day_inputs = open('input.txt', 'r')
inputs_list = day_inputs.readlines()
instructions_data = []

for i in inputs_list:
    if i != "\n":
        instruction = [i[0], int(i[1:len(i)-1])]
        instructions_data.append(instruction)

x_delta = 0
y_delta = 0
waypoint_x_delta = 10
waypoint_y_delta = 1

# Action N means to move the waypoint north by the given value.
# Action S means to move the waypoint south by the given value.
# Action E means to move the waypoint east by the given value.
# Action W means to move the waypoint west by the given value.
# Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
# Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
# Action F means to move forward to the waypoint a number of times equal to the given value.

# float s = sin(angle); // angle is in radians
# float c = cos(angle); // angle is in radians

# For clockwise rotation :
#
# float xnew = p.x * c + p.y * s;
# float ynew = -p.x * s + p.y * c;

# For counter clockwise rotation :
#
# float xnew = p.x * c - p.y * s;
# float ynew = p.x * s + p.y * c;

for instruction in instructions_data:
    action = instruction[0]
    value = instruction[1]

    if action == 'N':
        waypoint_y_delta += value
    if action == 'S':
        waypoint_y_delta -= value
    if action == 'E':
        waypoint_x_delta += value
    if action == 'W':
        waypoint_x_delta -= value
    if action == 'L': # counter-clockwise rotation
        original_x = waypoint_x_delta
        original_y = waypoint_y_delta
        radians = math.radians(value)
        waypoint_x_delta = math.cos(radians) * original_x - math.sin(radians) * original_y
        waypoint_y_delta = math.sin(radians) * original_x + math.cos(radians) * original_y
    if action == 'R': # clockwise rotation
        original_x = waypoint_x_delta
        original_y = waypoint_y_delta
        radians = math.radians(value)
        waypoint_x_delta = math.cos(radians) * original_x + math.sin(radians) * original_y
        waypoint_y_delta = math.sin(radians) * -original_x + math.cos(radians) * original_y
    if action == 'F':
        x_delta += (value * waypoint_x_delta)
        y_delta += (value * waypoint_y_delta)

manhattan_distance = abs(x_delta) + abs(y_delta)
print(manhattan_distance)

day_inputs.close()
