from scipy import integrate
from Exercise_2_1 import *
from time import time

# a)
def trapezium_adaptive(f, a, b, eta, *args):
    return Trapezium(f, a, b, eta), abs(integrate.quad(f, a, b)[0] - Trapezium(f, a, b, eta))
I = trapezium_adaptive(lambda x: x**2, 0.0, 2.0, 5)
print 'I = trapezium_adaptive(lambda x: x**2, 0.0, 2.0, 5) = ', I
i, e = trapezium_adaptive(lambda x: x**2, 0.0, 2.0, 5)
print 'i,e = trapezium_adaptive(lambda x: x**2, 0.0, 2.0, 5), i = ',i, ' e = ', e
print
print
# b)
def simpson_adaptive(f, a, b, eta, *args):
    return Simpson(f, a, b, eta), abs(integrate.quad(f, a, b)[0] - Simpson(f, a, b, eta))

II = simpson_adaptive(lambda x: x**2, 0.0, 2.0, 5)
print 'I = simpson_adaptive(lambda x: x**2, 0.0, 2.0, 5) = ', II
ii, ee = simpson_adaptive(lambda x: x**2, 0.0, 2.0, 5)
print 'i,e = simpson_adaptive(lambda x: x**2, 0.0, 2.0, 5), i = ', ii, ' e = ', ee

# c)
print
print
t1 = time()
i, e = trapezium_adaptive(lambda x: x**2, 0.0, 2.0, 5)
t2 = time()
print 'trapezium_adaptive takes ', t2 - t1, 's to be completed.'
print
print
t3 = time()
i, e = simpson_adaptive(lambda x: x**2, 0.0, 2.0, 5)
t4 = time()
print 'simpson_adaptive takes ', t4 - t3, 's to be completed.'