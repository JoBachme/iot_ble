import numpy as np

def trilateration(ref_points, distances):
    num_points = len(ref_points)

    # Construct the matrix A and vector b for solving the equations Ax = b
    A = np.zeros((num_points - 1, 3))
    b = np.zeros((num_points - 1, 1))
    for i in range(num_points - 1):
        A[i, :] = 2 * (ref_points[i + 1] - ref_points[0])
        b[i] = np.linalg.norm(ref_points[0]) ** 2 - np.linalg.norm(ref_points[i + 1]) ** 2 - distances[0] ** 2 + distances[i + 1] ** 2

    # Solve the system of equations using least squares optimization
    x = np.linalg.lstsq(A, b, rcond=None)[0]

    # Calculate the coordinates of the unknown point
    unknown_point = x.flatten()

    return unknown_point

# Example usage
# Define the known reference points and distances
ref_points = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]])  # Coordinates of reference points
distances = np.array([2, 2, 2, 2])  # Distances from the reference points to the unknown point

# Calculate trilateration
unknown_point = trilateration(ref_points, distances)

# Print the coordinates of the unknown point
print("Coordinates of the unknown point:", unknown_point)

#TODO We need a function to get a distance from the reference point to the unknown point with the RSSI value