from matplotlib import pyplot as plt
import json
import os
import numpy as np
import pandas as pd

DIRECTORY = "Messungen"

def create_messung_dict(filename):
    data_array = []
    dataset = dict()
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
    print("Durchschnitt: ", np.mean(data_array))
    print("Median: ", np.median(data_array))
    print("Std: ", np.std(data_array))
    print(f"Untere Grenze: {data_array[0]}, Obere Grenze: {data_array[-1]}")

    # plt.boxplot(dataset)
    # plt.show()

    return data_array

plt.rcParams["figure.figsize"] = [10, 3.50]
plt.rcParams["figure.autolayout"] = True

data = dict()
fig, ax = plt.subplots()

for filename in os.listdir(DIRECTORY):
    f = os.path.join(DIRECTORY, filename)
    arr = create_messung_dict(f)
    f = int(f.split("_")[1][:-2])
    data[f] = arr

data = dict(sorted(data.items()))
ax.boxplot(data.values())
ax.set_xticklabels(data.keys())

plt.show()

# Nur ein Protokoll auswählen aus den ganzen Paketen
# https://stackoverflow.com/questions/32735016/how-to-identify-a-eddystone-via-scanrecord/66703766#66703766
    