import numpy as np
import os
from scipy.optimize import curve_fit
from curve_calculation import create_messung_dict
import matplotlib.pyplot as plt
import csv
from pathlib import Path
from calculate_distance import calculate_rssi_value_from_distance
from utils import data_extraction


THIS_FILE = Path(__file__).parent.resolve()
DIR_TRAINING = THIS_FILE / "../Messungen/1Messung_Training"
DIR_TEST = THIS_FILE / "../Messungen/1Messung_Test"
DIR_2TRAINING = THIS_FILE / "../Messungen/2Messung_Training"
mess_abstaende = [0, 5, 10, 12.5, 15, 17.5, 20, 22, 24, 26, 27]

def log_distance_path_loss(d, RSSI0, n, d0):
    return RSSI0 - 10 * n * np.log10(d / d0)

def create_messung_dict(DIRECTORY):
    data = dict()
    for filename in os.listdir(DIRECTORY):
        f = os.path.join(DIRECTORY, filename)
        print(f)
        arr = data_extraction(f)
        f = int(f.split("_")[-2][:-2])
        data[f] = arr
    return data

data = create_messung_dict(DIR_TRAINING)
test = create_messung_dict(DIR_TEST)
fig, ax = plt.subplots()

data = dict(sorted(data.items()))
test = dict(sorted(test.items()))

y_values = []
for datalist in data.values():
    y_values.append(np.median(datalist))


x_value = [ x / 100 for x in list(data.keys())]

initial_guess = [ -30, 2, 0.05]

params, _ = curve_fit(
    log_distance_path_loss,
    x_value,
    y_values,
    p0=initial_guess,
)



x_data_lin = np.linspace(0.01, 8, num=800)
# Generate predicted RSSI values using the estimated parameters
predicted_RSSI_values = log_distance_path_loss(x_data_lin, params[0], params[1], params[2] )

test = create_messung_dict(DIR_TEST)
test = dict(sorted(test.items()))


# Plot the original data and the fitted curve
# plt.scatter(x_data, y_data, label='Measured RSSI')
plt.plot(x_data_lin, predicted_RSSI_values, 'r-', label='Fitted Curve')
plt.scatter(x_value, y_values, color='blue')

plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(2.0)  # X-axis line width
ax.spines['left'].set_linewidth(2.0)
plt.xlabel('Distance [m]', fontsize=16)
plt.ylabel('RSSI [dBm]', fontsize=16)
plt.show()

print(params)