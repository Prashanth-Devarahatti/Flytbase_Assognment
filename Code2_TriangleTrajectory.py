
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import argparse
from flyt_python import api

# Initialize the drone navigation API
drone = api.navigation(timeout=120000)

# Ensure the drone interface initializes properly
time.sleep(3)

# Parsing command line arguments
parser = argparse.ArgumentParser(description='Process a float value.')
parser.add_argument('side', metavar='side_length', type=float, help='side length of the triangle')
args = parser.parse_args()

# Assign side length from parsed arguments
side_length = args.side

# Calculate the coordinates for the triangle (equilateral triangle)
x1 = side_length
y1 = 0
x2 = -0.5 * side_length
y2 = (3**0.5 / 2) * side_length
x3 = -0.5 * side_length
y3 = -(3**0.5 / 2) * side_length

# Takeoff to 10 meters
print("Taking off!")
drone.take_off(10.0)

# Move in a triangle trajectory with specified side length
print('Flying in a triangle with side length', side_length)
drone.position_set(x1, y1, 0, relative=True)
drone.position_set(x2 - x1, y2 - y1, 0, relative=True)
drone.position_set(x3 - x2, y3 - y2, 0, relative=True)

# Land the drone
print("Landing")
drone.land(async=False)
print('Cheers!!')

# Shutdown the drone instance
drone.disconnect()
