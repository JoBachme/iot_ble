import numpy as np
import math

""" calculate the distance from a given rssi value based on the groundtruth data and curve fit """
# RSSI0 value is -24.35
# path loss exponent = 2.4949
# reference distance = 0.038

def calculate_rssi_value_from_distance(distance):
    return -24.35 - 10 * 2.4949 * np.log10(distance / 0.038)

def calculate_distance_from_rssi(rssi):
  return 0.038 * math.pow(10, ((-24.35 - rssi) / (10 * 2.4949)))
