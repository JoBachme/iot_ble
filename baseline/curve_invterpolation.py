import numpy as np
import os
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import csv

script_directory = os.path.dirname(os.path.abspath(__file__))


def log_distance_path_loss(d, RSSI0, n, d0):
    return RSSI0 - 10 * n * np.log10(d / d0)

ground_truth_data = os.path.join(script_directory, 'groundtruth2.csv')
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

initial_guess = [ -30, 2.46, 0.05]  # Initial parameter guesses [RSSI0, n, d0]

params, _ = curve_fit(
    log_distance_path_loss,
    x_data,
    y_data,
    p0=initial_guess,
)

# Extract the estimated parameters
RSSI0_est, n_est, d0_est = params

# Generate predicted RSSI values using the estimated parameters
predicted_RSSI_values = log_distance_path_loss(x_data, RSSI0_est, n_est, d0_est)

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Measured RSSI')
plt.plot(x_data, predicted_RSSI_values, 'r-', label='Fitted Curve')
plt.xlabel('Distance')
plt.ylabel('RSSI')
plt.legend()
plt.show()

# Print the estimated parameters
print('Estimated RSSI0:', RSSI0_est)
print('Estimated n:', n_est)
print('Estimated d0:', d0_est)
