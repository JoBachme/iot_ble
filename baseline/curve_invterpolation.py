import numpy as np
import os
from scipy.optimize import curve_fit
from curve_calculation import create_messung_dict
import matplotlib.pyplot as plt
import csv
from pathlib import Path

script_directory = os.path.dirname(os.path.abspath(__file__))
THIS_FILE = Path(__file__).parent.resolve()
DIR_TEST = THIS_FILE / "../Messungen/1Messung_Test"


def log_distance_path_loss(d, RSSI0, n, d0):
    return RSSI0 - 10 * n * np.log10(d / d0)

ground_truth_data = os.path.join(script_directory, 'groundtruth.csv')
x_data = []
y_data = []

with open(ground_truth_data, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row   
    for row in reader: 
        value1 = float(row[0])  
        value2 = float(row[1]) 
        
        if value1 == 0: #first values cannot be 0
            continue
        x_data.append(value1)
        y_data.append(value2)

x_data = np.array(x_data) # first parameter cannot be 0
y_data = np.array(y_data)

# average y values --------------------
averaged_values = {}
for x, y in zip(x_data, y_data):
    if x in averaged_values:
        averaged_values[x].append(y)  # Add the y-value to the existing list for that x-value
    else:
        averaged_values[x] = [y]  # Create a new list for that x-value

x_data = []
y_data = []
# Calculate the average of y-values for each x-value
for x, y_list in averaged_values.items():
    average_y = np.median(y_list)#sum(y_list) / len(y_list)
    x_data.append(x)
    y_data.append(average_y)
# end average --------------------------------

initial_guess = [ -30, 2, 0.05]  # Initial parameter guesses [RSSI0, n, d0]

params, _ = curve_fit(
    log_distance_path_loss,
    x_data,
    y_data,
    p0=initial_guess,
)

# Extract the estimated parameters
RSSI0_est, n_est, d0_est = params

x_data_lin = np.linspace(0.01, 8, num=800)
# Generate predicted RSSI values using the estimated parameters
predicted_RSSI_values = log_distance_path_loss(x_data_lin, RSSI0_est, n_est, d0_est)

plt.rcParams["figure.figsize"] = [10, 3.50]
plt.rcParams["figure.autolayout"] = True

test = create_messung_dict(DIR_TEST)
test = dict(sorted(test.items()))

for arr in list(zip(list(test.values()), list(test.keys()))):
    y = np.median(arr[0])
    x = arr[1] / 100
    plt.plot(x, y, marker="o", markersize=5, color="red")

# Plot the original data and the fitted curve
# plt.scatter(x_data, y_data, label='Measured RSSI')
plt.plot(x_data_lin, predicted_RSSI_values, 'r-', label='Fitted Curve')

plt.xlabel('Distance')
plt.ylabel('RSSI')
plt.legend()
plt.show()

# Print the estimated parameters
print('Estimated RSSI0:', RSSI0_est)
print('Estimated n:', n_est)
print('Estimated d0:', d0_est)
