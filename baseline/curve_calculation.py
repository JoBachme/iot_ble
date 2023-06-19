from matplotlib import pyplot as plt
from pathlib import Path
import json
import os
import numpy as np
import pandas as pd

THIS_FILE = Path(__file__).parent.resolve()
DIR_TRAINING = THIS_FILE / "../Messungen/1Messung_Training"
DIR_TEST = THIS_FILE / "../Messungen/1Messung_Test"
DIR_2TRAINING = THIS_FILE / "../Messungen/2Messung_Training"
mess_abstaende = [0, 5, 10, 12.5, 15, 17.5, 20, 22, 24, 26, 27]

def messung(filename):
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
    print("Durchschnitt: ", np.mean(data_array))
    print("Median: ", np.median(data_array))
    print("Std: ", np.std(data_array))
    print(f"Untere Grenze: {data_array[0]}, Obere Grenze: {data_array[-1]}")
    print()

    return data_array

def create_messung_dict(DIRECTORY):
    data = dict()
    for filename in os.listdir(DIRECTORY):
        f = os.path.join(DIRECTORY, filename)
        print(f)
        arr = messung(f)
        f = int(f.split("_")[-2][:-2])
        data[f] = arr
    return data

plt.rcParams["figure.figsize"] = [10, 3.50]
plt.rcParams["figure.autolayout"] = True

data = create_messung_dict(DIR_TRAINING)
test = create_messung_dict(DIR_TEST)
fig, ax = plt.subplots()

data = dict(sorted(data.items()))
test = dict(sorted(test.items()))
ax.boxplot(data.values())
ax.set_xticklabels(data.keys())

plt.plot(5, -40, marker="o", markersize=5, markeredgecolor="red")

for arr in list(zip(list(test.values()), mess_abstaende)):
    y = np.median(arr[0])
    x = arr[1]+1
    plt.plot(x, y, marker="o", markersize=5, markeredgecolor="red")

plt.show()

# Nur ein Protokoll auswählen aus den ganzen Paketen
# https://stackoverflow.com/questions/32735016/how-to-identify-a-eddystone-via-scanrecord/66703766#66703766
    