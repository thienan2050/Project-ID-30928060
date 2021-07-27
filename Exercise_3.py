import numpy as np 
import matplotlib.pyplot as plt 

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

f = lambda t, x : LotkaVolteraModel(x, 1.1, 0.4, 0.4, 0.1)
x0 = np.array([20, 5])
t0 = 0
tf = 30
dt = 0.001

x, t = RungeKutta4(f, x0, t0, tf, dt)

plt.subplot(1, 2, 1)
plt.plot(t, x[0,:], 'r', label = 'Preys')
plt.plot(t, x[1,:], 'g', label = 'Predators')
plt.xlabel('Time (t)')
plt.grid()
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x[0,:], x[1,:])
plt.xlabel('Preys')
plt.ylabel('Predators')
plt.grid()
plt.show()