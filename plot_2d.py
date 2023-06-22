import numpy as np
import os
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import csv
from pathlib import Path
import matplotlib.patches as patches

def plot2D(points, true_point):
  x_points = points[:,0] / 100
  y_points = points[:,1] / 100

  plt.subplot()
  plt.scatter(x_points, y_points, color="blue", label="Errechnete Positionen")
  plt.scatter(true_point[0] / 100, true_point[1] / 100, color="r", s=100, label="Tatsächliche Position")

  plt.xlim(-0.30, 1.30)
  plt.ylim(-0.30, 1.30)

 

  square = patches.Rectangle((-0.05,-0.05), 0.10, 0.10, edgecolor='grey', facecolor='none')
  square2 = patches.Rectangle((0.95,0.95), 0.10, 0.10, edgecolor='grey', facecolor='none')
  square3 = patches.Rectangle((-0.05,0.95), 0.10, 0.10, edgecolor='grey', facecolor='none')
  square4 = patches.Rectangle((0.95,-0.05), 0.10, 0.10, edgecolor='grey', facecolor='none')

  ax = plt.gca()
  ax.add_patch(square)
  ax.add_patch(square2)
  ax.add_patch(square3)
  ax.add_patch(square4)
  ax.set_xticks([0,1])
  ax.set_yticks([0,1])
  plt.xlabel('Distanz [m]', fontsize=16)
  plt.ylabel('Distanz [m]', fontsize=16)
  plt.legend(fontsize=15)
  plt.show()