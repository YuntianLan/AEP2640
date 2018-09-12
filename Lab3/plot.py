import matplotlib.pyplot as plt
import numpy as np

xincr = 2e-6

with open('curve.txt') as f:
    for line in f:
        s = line

lst = s.split('\t')
lst[-1] = lst[-1][:-1]

volts = list(map(float, lst))
time = np.arange(0, 2e-6 * len(volts), 2e-6)

plt.plot(time, volts)
plt.show()