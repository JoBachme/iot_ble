""" example of how to get distance from rssi: """

from baseline.calculate_distance import calculate_distance_from_rssi, calculate_rssi_value_from_distance

rssi = -67
distance = 2
t_distance = calculate_distance_from_rssi(rssi)
t_rssi = calculate_rssi_value_from_distance(distance)

print(t_distance)
print(t_rssi)