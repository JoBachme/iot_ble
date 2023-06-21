import numpy as np
import os
import csv
import sys
module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'beacon_utils'))
sys.path.append(module_dir)
from filter_beacon_name import filter_beacon_name
from beacon_enum import Beacon
script_directory = os.path.dirname(os.path.abspath(__file__))

GROUND_TRUTH_FOLDER = "../Messungen/1Messung_Training"
ground_truth_path = os.path.join(script_directory, GROUND_TRUTH_FOLDER)
def get_data(filename):
    data_array = []

    with open(filename, "r", encoding="UTF-8") as file:
        json_file = file.readlines()
    
    for i, v in enumerate(json_file):
        beacon_name = filter_beacon_name(v)
        if beacon_name == Beacon.D:
            data_array.append(int(v.split("rssi=")[1].split(",")[0]))

    data_array = np.array(data_array)
    return data_array

distances = []
rssi_values = []
for filename in os.listdir(ground_truth_path):
    f = os.path.join(ground_truth_path, filename)
    curr_data = get_data(f)
    distance = int(filename.split("_")[1][:-2])
    distance = distance / 100.0
    distances.extend([distance for _ in range(len(curr_data))])
    rssi_values.extend(curr_data)

zipped_lists = zip(distances, rssi_values)
sorted_lists = sorted(zipped_lists)
distances, rssi_values = zip(*sorted_lists)

data = list(zip(distances, rssi_values))
filename = os.path.join(script_directory, 'groundtruth.csv')
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Distances', 'RSSI'])
    writer.writerows(data)