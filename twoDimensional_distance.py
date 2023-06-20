import csv
import numpy as np
from pathlib import Path
from enum import Enum

from baseline.calculate_distance import calculate_distance_from_rssi, calculate_rssi_value_from_distance
from baseline.utils import data_extraction_2d, calculate_distance_twoPoints, trilateration


THIS_FILE = Path(__file__).parent.resolve()
DIR_TRAINING = THIS_FILE / "Messungen/2DMessung_Training"

CUT_OFF_DISTANCE = 200

def main():
    filename = DIR_TRAINING / "1Messung_100_100.txt"
    data_dict = data_extraction_2d(filename)

    # Define the known reference points and distances
    ref_points = np.array([[0, 0, 0], [0, 100, 0], [100, 100, 0], [100, 0, 0]])
    possible_points = []

    # Trilateration over all points and afterwards calculate the median of all positions
    for v1, v2, v3, v4 in zip(data_dict["0_0"], data_dict["0_100"], data_dict["100_100"], data_dict["100_0"]):
        dC = round(calculate_distance_from_rssi(v1)*100, 2) # Distances from the reference points to the unknown point
        dD = round(calculate_distance_from_rssi(v2)*100, 2)
        dA = round(calculate_distance_from_rssi(v3)*100, 2)
        dB = round(calculate_distance_from_rssi(v4)*100, 2)
        distances = np.array([dC, dD, dA, dB])
        #added check to filter out outlier that have a distance above 2 meter
        if np.any(distances > CUT_OFF_DISTANCE):
            continue

        #print(f"==Distances from Unknown Point to every Beacon==")
        #print(f"Beacon C (0|0) {v1} -> {distances[0]}cm; Beacon D (0|100) {v2} -> {distances[1]}cm; Beacon A (100|100) {v3} -> {distances[2]}cm; Beacon B (100|0) {v4} -> {distances[3]}cm")

        # Calculate trilateration
        unknown_point = trilateration(ref_points, distances)
        unknown_point = [np.round(x, 3) for x in unknown_point]
        possible_points.append(unknown_point)
    
    # calculate the mean point over all points
    possible_points = np.array(possible_points)

    mean_point = np.mean(possible_points, axis=0)
    mean_point = [np.round(x, 3) for x in mean_point]
    print(f"Calculated Point by averaging the location of all points: {mean_point[:2]}") # Print the coordinates of the first calculated mean point


    distances = []
    # Trilateration from the Median of all distances
    for value in data_dict.values():
        distances_for_beacon = []
        for curr_rssi in value:
            curr_dist = calculate_distance_from_rssi(curr_rssi) * 100
            if curr_dist <= CUT_OFF_DISTANCE:
                distances_for_beacon.append(curr_dist)

        calculated_distance = round(np.mean(distances_for_beacon), 2)
        distances.append(calculated_distance)

    mean_point2 = trilateration(ref_points, distances)
    mean_point2 = [np.round(x, 3) for x in mean_point2]
    print(f"Average distances: {distances} leads to calculated point: {mean_point2[:2]}") # Print the coordinates of the second mean point

    #for ref in ref_points:
    #    print(calculate_distance_twoPoints(ref, unknown_point))



if __name__ == "__main__":
    main()