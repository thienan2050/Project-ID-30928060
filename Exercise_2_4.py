from scipy.integrate import quad
from numpy import sqrt, sin, cos, pi
import numpy as np
import math
import matplotlib.pyplot as plt

def Bessel(theta, m, x):
    return (1/pi)*(cos(m*theta - x*sin(theta)))
def J(m, x):
    return quad(Bessel, 0, pi, args=(m, x))[0]

#print J(1.0, 5.0)

# a)
x = np.linspace(0, 20, 100)
J0 = [J(0, _) for _ in x]
J1 = [J(1, _) for _ in x]
J2 = [J(2, _) for _ in x]
plt.xlim(0, 20)
plt.plot(x, J0, label = 'J0(x)')
plt.plot(x, J1, label = 'J1(x)')
plt.plot(x, J2, label = 'J2(x)')
plt.xlabel('x')
plt.grid()
plt.legend()
plt.show()

# b)
def Intensity(lamda, r):
    return (J(1, (2*pi*r)/lamda)/((2*pi*r)/lamda))**2

