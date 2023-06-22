import numpy as np
import os
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import csv

script_directory = os.path.dirname(os.path.abspath(__file__))


def calculate_rssi_value_from_distance(distance):
    return -37.9 - 10 * 1.89 * np.log10(distance / 0.05)

def calculate_rssi_value_from_distance_old(distance):
    return -31.55 - 10 * 2.745 * np.log10(distance / 0.0938)

x_data = np.linspace(0,6,num=50)

# Generate predicted RSSI values using the estimated parameters
predicted_RSSI_values = calculate_rssi_value_from_distance(x_data)
predicted_RSSI_values_old = calculate_rssi_value_from_distance_old(x_data)

# Plot the original data and the fitted curve
fig, ax = plt.subplots()

plt.rcParams["figure.figsize"] = [10, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.plot(x_data, predicted_RSSI_values_old, 'g-', label='P0=-31.55, alpha=2.745, d0=0.09')
plt.plot(x_data, predicted_RSSI_values, 'r', linestyle = '--', label='P0=-37.9, alpha=1.89, d0=0.05')

plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(2.0)  # X-axis line width
ax.spines['left'].set_linewidth(2.0)
plt.xlabel('Distance [m]', fontsize=16)
plt.ylabel('RSSI [dBm]', fontsize=16)
plt.legend(fontsize=15)
plt.show()

