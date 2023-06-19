from baseline.calculate_distance import calculate_distance_from_rssi, calculate_rssi_value_from_distance
from baseline.utils import data_extraction
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
filename_example = "Messungen/1Messung_Test/2M_100cm_0Tx.txt"
curr_data = data_extraction(filename_example)
median_rssi = np.median(curr_data)
calculated_distance = calculate_distance_from_rssi(median_rssi)

print(f"Calculated Distance: {round(calculated_distance*100, 2)}cm from RSSI Value: {median_rssi} | Real Distance: {filename_example.split('_')[2]}")