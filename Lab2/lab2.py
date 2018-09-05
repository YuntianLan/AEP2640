import numpy as np
from matplotlib import pyplot as plt

T = np.arange(0, 1.05, 0.05)
V = np.array([0.041, 0.128, 0.449, 0.748, 0.785, 0.831, 0.774, 0.643, 0.606,\
             0.187, 0.067, -0.332, -0.604, -0.688, -0.840, -0.818, -0.834,\
            -0.640, -0.567, -0.179, -0.080])

f2 = np.polyfit(T, V, 2, full = True)
f3 = np.polyfit(T, V, 3, full = True)
f4 = np.polyfit(T, V, 4, full = True)
f5 = np.polyfit(T, V, 5, full = True)

residual2 = f2[1][0]
residual3 = f3[1][0]
residual4 = f4[1][0]
residual5 = f5[1][0]

rms2 = np.sqrt(residual2 / len(T))
rms3 = np.sqrt(residual3 / len(T))
rms4 = np.sqrt(residual4 / len(T))
rms5 = np.sqrt(residual5 / len(T))

coe = f5[0]
c5, c4, c3, c2, c1, c0 = coe
func = lambda x: \
c5 * x**5 + c4 * x**4 + c3 * x**3 + c2 * x**2 + c1 * x + c0
V5 = list(map(func, list(T)))

plt.xticks(np.arange(0, 1.2, step = 0.2))
plt.yticks(np.arange(-1, 1.5, step = 0.5))
axes = plt.gca()
axes.set_ylim([-1,1])
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Polynomial Curve Fitting')

plt.plot(T, V, marker = 'o', linewidth = 0)
plt.plot(T, V5)

#plt.show()




# Solve for A
A = 0
for i in range(len(V)):
    if i % 10 != 0:
        A += (V[i] / np.sin(2 * np.pi * T[i]))

A /= 18

func = lambda x: A * np.sin(2 * np.pi * x)
Va = list(map(func, list(T)))

rmsa = np.sqrt(np.average((Va - V)**2))

plt.xticks(np.arange(0, 1.2, step = 0.2))
plt.yticks(np.arange(-1, 1.5, step = 0.5))
axes = plt.gca()
axes.set_ylim([-1,1])
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Sinusoidal Fitting')

plt.plot(T, V, marker = 's', linewidth = 0)
plt.plot(T, Va)

#plt.show()