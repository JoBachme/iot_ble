import numpy as np
import math

""" calculate the distance from a given rssi value based on the groundtruth data and curve fit """
# RSSI0 value is -24.35
# path loss exponent = 2.4949
# reference distance = 0.038

# For second measurement only within one meter we received the following values:
# RSSSIO = -33.3
# n = 1.959
# d0 = 0.0296

def calculate_rssi_value_from_distance(distance):
    return -33.3 - 10 * 1.959 * np.log10(distance / 0.0296)

def calculate_distance_from_rssi(rssi):
  return 0.0296 * math.pow(10, ((-33.3 - rssi) / (10 * 1.959)))
