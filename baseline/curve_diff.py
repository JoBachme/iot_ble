import numpy as np
import os
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import csv

script_directory = os.path.dirname(os.path.abspath(__file__))


def calculate_rssi_value_from_distance(distance):
    return -33.3 - 10 * 1.959 * np.log10(distance / 0.0296)

def calculate_rssi_value_from_distance_old(distance):
    return -24.35 - 10 * 2.4949 * np.log10(distance / 0.038)

x_data = np.linspace(0,6,num=50)

# Generate predicted RSSI values using the estimated parameters
predicted_RSSI_values = calculate_rssi_value_from_distance(x_data)
predicted_RSSI_values_old = calculate_rssi_value_from_distance_old(x_data)

# Plot the original data and the fitted curve
plt.rcParams["figure.figsize"] = [10, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.plot(x_data, predicted_RSSI_values_old, 'g-', label='Fitted Curve Old')
plt.plot(x_data, predicted_RSSI_values, 'r', linestyle = '--', label='Fitted Curve New')
plt.xlabel('Distance')
plt.ylabel('RSSI')
plt.legend()
plt.show()

