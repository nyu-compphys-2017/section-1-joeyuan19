# This is a python file! The '#' character indicates that the following line is a comment.

# The following is an example for how to define a function in Python
# def tells the compiler that hello_world is the name of a function
# this implementation of hello_world takes a string as an argument,
# which has default value of the empty string. If the user calls 
# hello_world() without an argument, then the compiler uses ''
# as the default value of the argument.
def hello_world(name=''):
    print "hello world!"
    print name
    return
    
    
#Implement the Riemann Sum approximation for integrals.
import matplotlib.pyplot as plt
import numpy as np

# No Numpy, explicit
def r_riemann(f,x0,x1,N):
    dx = (x1-x0)/N
    s = 0
    x = x0
    for i in range(N):
        s += f(x+dx)
        x += dx
    return s*dx

# No numpy, shorter
def short_r_riemann(f,x0,x1,N):
    dx = (x1-x0)/N
    return sum(f(x0+i*dx) for i in range(1,N+1))*dx

# With Numpy
def np_r_riemann(f,x0,x1,N):
    dx = (x1-x0)/N
    return np.sum(f(np.linspace(x0+dx,x1,N)))*dx

# Examples testing a function against each implementation above
x0 = -1
x1 = 1
N = 1000
f = lambda x : x**2 
RF = [r_riemann,short_r_riemann,np_r_riemann]
for rf in RF:
    print(rf)
    print(rf(f,x0,x1,N))

"""
# plotting convergence below.
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
for ri,pi in zip(r,plot_vars):
    print(ri)
