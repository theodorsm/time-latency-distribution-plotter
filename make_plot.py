#!./venv/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys
import os



# Read file from argument
path = str(sys.argv[1])
with open(path) as f:
    values = f.readlines()
values = [float(x.strip()) for x in values]

points = np.arange(1, len(values) + 1, step=1)

# Calculate the simple average of the data
value_mean = [np.mean(values)]*len(points)
fig,ax = plt.subplots()

# Plot the data
data_line = ax.plot(points, values, label="Data", marker="o")

# Plot the average line
mean_line = ax.plot(points, value_mean, label="Mean=" + str(round(value_mean[0], 4)), linestyle="--")

# Make a legend
legend = ax.legend(loc="upper right")

# Plot values
plt.plot(points, values, marker="o",color="b",linestyle="-")

# Make sure x-axis has correct steps
plt.xticks(points)

# Uncomment for grid
# plt.grid(color="r", linestyle=":", linewidth=1)

plt.xlabel("Packet count")
plt.ylabel("RTT in ms")
filename = "PLOT_" + os.path.basename(path)[:-4]
plt.savefig(filename + ".png")
