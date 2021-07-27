import math
import numpy as np
import matplotlib.pyplot as plt

# EXERCISE 2.2 MAXWELL SPEED DISTRIBUTION

# Constant
kB = 1.38e-23 # J/K^-1
PI = 3.141592654

# a)
def MaxwellSpeedDistribution(v, m, T):
    return 4*PI*((m/(2*PI*kB*T))**(1.5))*v*v*math.exp(-(m*v*v)/(2*kB*T))
# ---------------------------------------------------------------------------
# b)

# (i) 
v = np.arange(0, 100)
def f1(v):
    return 1.6243*np.exp(-9)*(v**2)*np.exp(-8.0314*np.exp(-7)*v**2)
plt.plot(v, f1(v))
#plt.show()

# (ii)
def f2(v):
    return 4.9352*np.exp(-9)*(v**2)*np.exp(-1.6848*np.exp(-6)*v**2)
plt.plot(v, f2(v))
#plt.show()

#-----------------------------------------------------------------------------------
# c)
# (i) Simpson's rule 
from Exercise_2_1 import *
print(Simpson(f1, 15.0, 25.0, 1000))
print(Simpson(f2, 15.0, 25.0, 1000))

# (ii) scipy.integrate.quad()
from scipy import integrate
print(integrate.quad(f1, 15, 25)[0])
print(integrate.quad(f2, 15, 25)[0])
plt.show()