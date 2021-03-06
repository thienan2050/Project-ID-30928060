import numpy as np 
import matplotlib.pyplot as plt 

# a) Solve equations
def LotkaVolteraModel(x, alpha, beta, gamma, delta):
    return np.array([alpha*x[0] - beta*x[0]*x[1], delta*x[0]*x[1] - gamma*x[1]])

def RungeKutta4(f, x0, t0, tf, dt):
    t = np.arange(t0, tf, dt)
    nt = t.size
    nx = x0.size 
    x = np.zeros((nx, nt))
    x[:, 0] = x0
    for k in range(nt - 1):
        k1 = dt*f(t[k], x[:,k])
        k2 = dt*f(t[k] + dt/2, x[:,k] + k1/2)
        k3 = dt*f(t[k] + dt/2, x[:,k] + k2/2)
        k4 = dt*f(t[k] + dt, x[:,k] + k3)
        dx = (k1 + 2*k2 + 2*k3 +k4)/6
        x[:, k+1] = x[:, k] + dx
    return x, t

f = lambda t, x : LotkaVolteraModel(x, 1, 0.5, 2, 0.5)
x0 = np.array([20, 5])
t0 = 0
tf = 30
dt = 0.001

x, t = RungeKutta4(f, x0, t0, tf, dt)

plt.subplot(1, 2, 1)
plt.plot(x[0,:], x[1,:])
plt.xlabel('rabbits')
plt.ylabel('foxes')
plt.grid()



# b) Graph 
from random import *
from numpy import *
import sys

# model parameters
a = 1
b = 0.5
c = 2
d = 0.5
dt = 0.0001
limitTime = 30

# initial time and populations
t = 0
x = 2
y = 2

t_list = []
x_list = []
y_list = []

# initialize lists
t_list.append(t)
x_list.append(x)
y_list.append(y)

while t < limitTime:
    t = t + dt
    x = x + (a*x - b*x*y)*dt
    y = y + (-c*y + d*x*y)*dt
    t_list.append(t)
    x_list.append(x)
    y_list.append(y)

plt.subplot(1, 2, 2)
plt.plot(t_list, x_list, 'r', label = 'rabbits')
plt.plot(t_list, y_list, 'g', label = 'foxes')
plt.xlabel('Time (t)')
plt.xlim(0, 30)
plt.grid()
plt.legend()
plt.show()
