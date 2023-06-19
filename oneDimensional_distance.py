""" example of how to get distance from rssi: """

from baseline.calculate_distance import calculate_distance_from_rssi, calculate_rssi_value_from_distance
from baseline.curve_calculation import messung
import numpy as np



# Test: Distance from RSSI value and RSSI value from distance
rssi = -67
distance = 2
t_distance = calculate_distance_from_rssi(rssi)
t_rssi = calculate_rssi_value_from_distance(distance)

print(f"==Example from Distance to RSSI Value==")
print(f"Calculated RSSI Value: {round(t_rssi, 2)} from Distacce: {distance*100}cm\n")

print(f"==Example from RSSI Value to Distance==")
print(f"Calculated Distance: {round(t_distance*100, 2)}cm from RSSI Value: {rssi}\n")

# Test: Distance from a File of RSSI Values
rssi_values = []
filename_example = "Messungen/1Messung_Test/2M_100cm_0Tx.txt"
curr_data = messung(filename_example)
rssi_values.extend(curr_data)

median_rssi = np.median(curr_data)
calculated_distance = calculate_distance_from_rssi(median_rssi)

print(f"Calculated Distance: {round(calculated_distance*100, 2)}cm from RSSI Value: {median_rssi} | real Distance: {filename_example.split('_')[2]}")