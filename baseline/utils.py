import numpy as np
import math
from scipy.optimize import minimize

""" calculate the distance from a given rssi value based on the groundtruth data and curve fit """
# RSSI0 value is -24.35
# path loss exponent = 2.4949
# reference distance = 0.038

# For second measurement only within one meter we received the following values:
# RSSSIO = -33.3
# n = 1.959
# d0 = 0.0296

def calculate_rssi_value_from_distance(distance):
    return -33.3 - 10 * 1.959 * np.log10(distance / 0.0296)

def calculate_distance_from_rssi(rssi):
  return 0.0296 * math.pow(10, ((-33.3 - rssi) / (10 * 1.959)))

def calculate_distance_twoPoints(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    distance = np.linalg.norm(point2 - point1)
    return distance

def data_extraction(filename):
    data_array = []
    count = 0

    with open(filename, "r", encoding="UTF-8") as file:
        json_file = file.readlines()
    
    for i, v in enumerate(json_file):
        data_array.append(int(v.split("rssi=")[1].split(",")[0]))
        count = i

    length = int(len(data_array)/2)
    data_array = data_array[length-50:length+50]
    data_array.sort()
    data_array = np.array(data_array)
    
    print("Anzahl Werte: ", count)
    print("Durchschnitt: ", round(np.mean(data_array), 2))
    print("Median: ", np.median(data_array))
    print("Std: ", round(np.std(data_array),2))
    print(f"Untere Grenze: {data_array[0]}, Obere Grenze: {data_array[-1]}")
    print()

    return data_array

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