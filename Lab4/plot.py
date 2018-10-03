import matplotlib.pyplot as plt
import numpy as np

xincr = 2e-5

with open('waveform_hardware.txt') as f:
    for line in f:
        s = line

lst = s.split('\t')
lst[-1] = lst[-1][:-1]
lst = lst[6:-1]

lst = lst[:500]

volts = list(map(float, lst))
volts = list(map(lambda x: x if x < 20 else x - 20.4, volts))
time = np.arange(0, xincr * len(volts), xincr)

plt.plot(time, volts)

plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Oscilloscope Reading')

plt.show()