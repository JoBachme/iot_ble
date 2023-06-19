from baseline.calculate_distance import calculate_distance_from_rssi, calculate_rssi_value_from_distance
from baseline.utils import data_extraction, calculate_distance_twoPoints, trilateration
import numpy as np

# Example usage
# Define the known reference points and distances
ref_points = np.array([[0, 0, 0], [100, 0, 0], [0, 100, 0], [100, 100, 0]])  # Coordinates of reference points
distances = np.array([(np.sqrt(2)/2)*50, (np.sqrt(2)/2)*50, (np.sqrt(2)/2)*50, (np.sqrt(2)/2)*50])  # Distances from the reference points to the unknown point
print(distances)

# Calculate trilateration
unknown_point = trilateration(ref_points, distances)
unknown_point = [np.round(x, 3) for x in unknown_point]

for ref in ref_points:
    print(calculate_distance_twoPoints(ref, unknown_point))

# Print the coordinates of the unknown point
print("Coordinates of the unknown point:", unknown_point)