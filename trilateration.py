import numpy as np
from scipy.optimize import minimize

def trilateration(ref_points, distances):
    num_points = len(ref_points)
    
    def distance_error(point):
        error = 0
        for i in range(num_points):
            distance_i = np.linalg.norm(ref_points[i] - point[:3])
            error += (distance_i - distances[i]) ** 2
        return error

    # Perform optimization to minimize the distance error
    initial_guess = np.mean(ref_points, axis=0)  # Initial guess for the unknown point
    result = minimize(distance_error, initial_guess, method='Nelder-Mead')

    # Retrieve the optimized unknown point coordinates
    unknown_point = result.x[:3]

    return unknown_point