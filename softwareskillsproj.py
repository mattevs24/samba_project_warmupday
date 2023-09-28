import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sympy as sp
#x=np.linspace(0,1,100)
#y=np.linspace(0,1,100)
#axes = plt.axes()
#ax = plt.axes(projection="3d")
#axes.set_xlim([0, 1])
#plt.plot(1/((np.sin(x))**2 + (np.sin(y))**2 ))
#plt.show()

##numerical solution
N = 10000
accum = 0
for i in range(N):
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)
    accum += 1/(1+ np.sin(x**2) + np.sin(y**2)) 
estimate=accum/float(N)
#print(estimate)

##analytical solution

#x = sp.Symbol("x")
#y = sp.Symbol("y")
#float(sp.integrate(1/(1+ sp.sin(x**2) + sp.sin(y**2)), (x, 0, 1), (y, 0, 1))

N = 100
accum = 0
for i in range(N):
    x = np.random.normal(0, 1)
    y = np.random.normal(0, 1)
    accum += x**2 +3*x*y -y**4
known_estimate=accum/float(N)
print(known_estimate)

x=np.random.normal(0,1,100)
if abs(x[i])>1:
    x.remove(x[i])

    
print(x)
#print(y)

#x = sp.Symbol("x")
#y = sp.Symbol("y")
#print(float(sp.integrate((x**2) + (3*x*y) - (y**4), (x, 0, 1), (y, 0, 1))))


