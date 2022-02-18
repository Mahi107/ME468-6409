#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import matplotlib.pyplot as plt
import math
import sys

h= float(sys.argv[1])      # integration time step
tend= float(sys.argv[2])   # duration of simluation
tm= np.arange(0,tend+h,h)
pngYesNo= int(sys.argv[3])

mass= 1000
stiff= 50000
damp= 4000

def ydot(time, u, x):
    f0= -(4*damp/mass)*u-(4*stiff/mass)*(x-0.4)-(10/4)
    returnnp.array(([f0], [u]))
    
y= np.zeros((2, tm.size))
y[0,0] = 0 # initial velocity
y[1,0] = 0.4 # initial position
for i in np.arange(1,tm.size):
    y_dot= ydot(tm[i], y[0, i], y[1, i])
    y[0, i] = y[0, i-1] + h* y_dot[0,0]
    y[1, i] = y[1, i-1] + h* y_dot[1,0]
        
plt.plot(tm,y[1,:])
if pngYesNo== 1:
    plt.savefig("plot.png")
    else:
        plt.show()

