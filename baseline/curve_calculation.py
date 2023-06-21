from matplotlib import pyplot as plt
from pathlib import Path
from utils import data_extraction
import json
import os
import numpy as np
import pandas as pd
import matplotlib



THIS_FILE = Path(__file__).parent.resolve()
DIR_TRAINING = THIS_FILE / "../Messungen/1Messung_Training"
DIR_TEST = THIS_FILE / "../Messungen/1Messung_Test"
DIR_2TRAINING = THIS_FILE / "../Messungen/2Messung_Training"
mess_abstaende = [0, 5, 10, 12.5, 15, 17.5, 20, 22, 24, 26, 27]



def create_messung_dict(DIRECTORY):
    data = dict()
    for filename in os.listdir(DIRECTORY):
        f = os.path.join(DIRECTORY, filename)
        print(f)
        arr = data_extraction(f)
        f = int(f.split("_")[-2][:-2])
        data[f] = arr
    return data

def main():
    plt.rcParams["figure.figsize"] = [10, 3.50]
    plt.rcParams["figure.autolayout"] = True

    data = create_messung_dict(DIR_TRAINING)
    test = create_messung_dict(DIR_TEST)
    fig, ax = plt.subplots()
    box_widths = [x for x in range(1, len(list(data.keys()))+1)]

    data = dict(sorted(data.items()))
    test = dict(sorted(test.items()))

    ax.boxplot(data.values(), positions=list(data.keys()), widths=box_widths)

    # for arr in list(zip(list(test.values()), mess_abstaende)):
    #     y = np.median(arr[0])
    #     x = arr[1]+1
    #     plt.plot(x, y, marker="o", markersize=5, markeredgecolor="red")

    plt.xscale('log', base=100)
    plt.show()

if __name__ == "__main__":
    main()

# Nur ein Protokoll auswählen aus den ganzen Paketen
# https://stackoverflow.com/questions/32735016/how-to-identify-a-eddystone-via-scanrecord/66703766#66703766
    