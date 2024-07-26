
!/usr/bin/env python
import time
from flyt_python import api

# Initialize the drone navigation API
drone = api.navigation(timeout=120000)

# Ensure the drone interface initializes properly
time.sleep(3)

# Takeoff to 5 meters
print('Taking off')
drone.take_off(5.0)

# Move in a square trajectory with 6.5m side length
print('Moving in a square trajectory')
drone.position_set(6.5, 0, 0, relative=True)
drone.position_set(0, 6.5, 0, relative=True)
drone.position_set(-6.5, 0, 0, relative=True)
drone.position_set(0, -6.5, 0, relative=True)

# Land the drone
print('Landing')
drone.land(async=False)

# Shutdown the drone instance
drone.disconnect()



