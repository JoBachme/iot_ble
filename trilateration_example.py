import numpy as np
from scipy.optimize import minimize

def trilateration(ref_points, distances):
    num_points = len(ref_points)
    
    def distance_error(point):
        error = 0
        for i in range(num_points):
            distance_i = np.linalg.norm(ref_points[i] - point[:3])
            error += (distance_i - distances[i]) ** 2
        return error

    # Perform optimization to minimize the distance error
    initial_guess = np.mean(ref_points, axis=0)  # Initial guess for the unknown point
    result = minimize(distance_error, initial_guess, method='Nelder-Mead')

    # Retrieve the optimized unknown point coordinates
    unknown_point = result.x[:3]

    return unknown_point

def calculate_distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    distance = np.linalg.norm(point2 - point1)
    return distance

# Example usage
# Define the known reference points and distances
ref_points = np.array([[0, 0, 0], [100, 0, 0], [0, 100, 0], [100, 100, 0]])  # Coordinates of reference points
distances = np.array([(np.sqrt(2)/2)*50, (np.sqrt(2)/2)*50, (np.sqrt(2)/2)*50, (np.sqrt(2)/2)*50])  # Distances from the reference points to the unknown point
print(distances)

# Calculate trilateration
unknown_point = trilateration(ref_points, distances)
unknown_point = [np.round(x, 3) for x in unknown_point]

for ref in ref_points:
    print(calculate_distance(ref, unknown_point))

# Print the coordinates of the unknown point
print("Coordinates of the unknown point:", unknown_point)