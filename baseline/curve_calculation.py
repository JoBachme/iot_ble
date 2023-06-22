from matplotlib import pyplot as plt
from pathlib import Path
from utils import data_extraction
import json
import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.ticker as ticker


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
    #box_widths = [x for x in range(1, len(list(data.keys()))+1)]
    box_widths = 0.07

    data = dict(sorted(data.items()))
    test = dict(sorted(test.items()))

    x_data = [ x / 100 for x in list(data.keys())]
    ax.boxplot(data.values(), positions=x_data, widths=box_widths)

    # for arr in list(zip(list(test.values()), mess_abstaende)):
    #     y = np.median(arr[0])
    #     x = arr[1]+1
    #     plt.plot(x, y, marker="o", markersize=5, markeredgecolor="red")

    #plt.xscale('log', base=1.5)
    desired_ticks =list(filter(lambda x: x not in [0.1, 0.3, 0.5, 0.7, 0.9], x_data))
    desired_ticks.append(0)
    ax.set_xticks(desired_ticks)
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))

    ax.spines['bottom'].set_linewidth(2.0)  # X-axis line width
    ax.spines['left'].set_linewidth(2.0)
    
    plt.rcParams['axes.labelsize'] = 16

    plt.tick_params(axis='x', labelsize=15)
    plt.tick_params(axis='y', labelsize=15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlabel('Distance [m]', fontsize=16)
    plt.ylabel('RSSI [dBm]', fontsize=16)
    plt.show()

if __name__ == "__main__":
    main()

# Nur ein Protokoll auswählen aus den ganzen Paketen
# https://stackoverflow.com/questions/32735016/how-to-identify-a-eddystone-via-scanrecord/66703766#66703766
    