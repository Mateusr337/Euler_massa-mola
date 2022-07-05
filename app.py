import numpy as np
import matplotlib.pyplot as plt

delta_t = 0.01
n_steps = 10000
k = 1
m = 1
x0 = 1
v0 = 0


def velocity_line_a(x):
    return - (k * x / m)


def Energy(v, x):
    energy = []

    for i in range(len(v)):
        Et = (0.5 * k * (x[i] ** 2)) + (0.5 * m * (v[i] ** 2))
        energy.append(Et)

    return energy


def Euler(n_steps, delta_t, v0, x0, a):
    v = [v0]
    x = [x0]
    t_interval = [0]

    for i in range(1, n_steps - 1):
        t = i*delta_t

        new_v = v[i - 1] + a(x[i - 1]) * delta_t
        new_x = x[i - 1] + v[i - 1] * delta_t

        v.append(new_v)
        x.append(new_x)
        t_interval.append(t)

    return {"v": v, "x": x, 't': t_interval}


euler = Euler(n_steps, delta_t, v0, x0, velocity_line_a)


plt.plot(euler["t"], euler["v"])
plt.plot(euler["t"], euler["x"])
plt.show()


energy = Energy(euler["v"], euler["x"])

plt.plot(euler["t"], energy)
plt.show()
