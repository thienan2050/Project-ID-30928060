
import matplotlib.pyplot as plt
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

plt.plot(t_list, x_list, 'g', t_list, y_list, 'b', linewidth = 3)
plt.show()