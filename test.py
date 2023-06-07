""" example of how to get distance from rssi: """

from baseline.calculate_distance import calculate_distance_from_rssi, calculate_rssi_value_from_distance
import numpy as np

rssi = -67
distance = 2
t_distance = calculate_distance_from_rssi(rssi)
t_rssi = calculate_rssi_value_from_distance(distance)

#print(t_distance)
#print(t_rssi)

def get_data(filename):
    data_array = []

    with open(filename, "r", encoding="UTF-8") as file:
        json_file = file.readlines()
    
    for i, v in enumerate(json_file):
        data_array.append(int(v.split("rssi=")[1].split(",")[0]))

    data_array = np.array(data_array)
    return data_array

rssi_values = []
filename = "Messungen/1Messung_Test/2M_100cm_0Tx.txt"
curr_data = get_data(filename)
rssi_values.extend(curr_data)

mean_rssi = np.mean(curr_data)
print(curr_data)
print(f"Mean RSSI Value: {mean_rssi}")

calculated_distance = calculate_distance_from_rssi(mean_rssi)
#calculated_distance = calculate_distance_from_rssi(-40)

print(f"Calculated Distance: {calculated_distance} from File: {filename}")

