#!./venv/bin/python

import ctypes as ct
import os
import sys

import colorcet as cc
import datashader as ds
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def convert(i):
    # i = int(s, 16)  # convert from hex to a Python int
    cp = ct.pointer(ct.c_int(i))  # make this into a c integer
    fp = ct.cast(cp, ct.POINTER(ct.c_float))  # cast the int pointer to a float pointer
    return round(fp.contents.value, 8)  # micro seconds


path = str(sys.argv[1])
times = []
lats = []
start_time = 0

with open(path, "br") as f:
    data = f.read(4)
    i = 0
    while data:
        number = int.from_bytes(data, "little")
        sample = convert(number)
        if i == 0:
            start_time = sample
        if i % 2 == 0:
            times.append(sample - start_time)
        else:
            lats.append(sample * 10 ** 3)
        data = f.read(4)
        i += 1
        #        if i == 50000:
        #            break
        # if i == 200000:
        #    break

# times = times[-400000:]
# lats = lats[-400000:]
length_time = len(times)
length_lats = len(lats)

# times = times[: length_time // 60]
# lats = lats[: length_lats // 60]

print(len(times))
print(len(lats))

df = pd.DataFrame({"x": times, "y": lats})  # create a DF from array
# sns.kdeplot(data=df, x="x", y="y", cmap="Reds", shade=True)
fig, ax = plt.subplots()
fig.set_size_inches(100.0, 6.0)
# fig.set_size_inches(350.0, 10.0)
mpl.rcParams["agg.path.chunksize"] = 200
plt.plot(
    "x", "y", "", data=df, marker="o", markersize=2, alpha=0.1, color="purple",
)
plt.xlabel("Packet rx timestamp (s)")
plt.ylabel("RTT in ms")
plt.xticks(np.arange(times[0], times[-1], 0.5))
# plt.xticks(np.arange(times[0], times[-1], 0.01))
filename = str(sys.argv[2])
filename = "plots/PLOT_" + os.path.basename(filename)
plt.savefig(filename + ".png", dpi=180)
