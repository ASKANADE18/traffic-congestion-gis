# congestion_index.py

# Importing NumPy for efficient numerical operations
import numpy as np

# Define an array of average vehicle speeds at various intersections (in km/h)
speed = np.array([45, 25, 10, 60])

# Define an array of vehicle counts observed at the same intersections
vehicle_count = np.array([20, 50, 100, 15])

# Congestion Index formula:
# Higher vehicle count and lower speed indicate higher congestion
# So we use: congestion_index = vehicle_count * (1 / speed)
congestion_index = vehicle_count * (1 / speed)

# Print the result to see congestion levels at each location
print("Congestion Index:", congestion_index)
