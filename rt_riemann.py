import matplotlib.pyplot as plt
import numpy as np

# No Numpy, explicit
def r_riemann(f,x0,x1,N):
    dx = (x1-x0)/N
    s = 0
    x = x0
    for i in range(N):
        s += f(x+dx)*dx
        x += dx
    return s

# No numpy, shorter
def short_r_riemann(f,x0,x1,N):
    dx = (x1-x0)/N
    return sum(f(x0+i*dx) for i in range(1,N+1))*dx

# With Numpy
def np_r_riemann(f,x0,x1,N):
    dx = (x1-x0)/N
    return np.sum(f(np.linspace(x0,x1,N,endpoint=False)+dx)*dx)

# Examples
x0 = -1
x1 = 1
N = 1000
f = lambda x : x**2 
RF = [r_riemann,short_r_riemann,np_r_riemann]
plot_vars = [('simple','r'),('short','g'),('numpy','b')]
M = 6
n = np.zeros(M)
r = np.zeros((3,M))

for e in range(1,M+1):
    N = 10**e
    n[e-1] = N
    for i,rf in enumerate(RF):
        _r = rf(f,x0,x1,N)
        print(rf,_r,N)
        #r[i,e-1] = rf(f,x0,x1,N)
        r[i,e-1] = _r 


print(r)
for ri,pi in zip(r,plot_vars):
    print(ri)
    l,c = pi
    plt.plot(n,ri,c+'o',label=l)
plt.show()
