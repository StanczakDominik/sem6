import numpy as np
import matplotlib.pyplot as plt
a = 1
B = 1
r = np.ones(2)
T = 100
t = 0
def f(r, t):
    x, v = r
    return np.array([v, -a*(v+x*(x*x-1)) + B*np.cos(2*np.pi/T*t)])

NT = 10000
dt = 0.1
FlashEveryNIterations = T/dt
r_history = np.zeros((NT,2))
r_history[0] = r

for i in range(1,NT):
    r += f(r,t) * dt
    t += dt
    r_history[i] = r

theta, omega = r_history[:, :].T

plt.plot(theta, omega)

theta2, omega2 = r_history[::FlashEveryNIterations, :].T
plt.scatter(theta2, omega2)
plt.grid()
plt.show()
