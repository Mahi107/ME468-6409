#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
def func(x):
    return math.exp(x)-4
def bisection(X_low,X_high):
    if (func(X_low) * func(X_high) >= 0):
        print("You have not assumed right X_low and X_high\n")
        return
    c = X_low
    while ((X_high-X_low) >= 0.01):
        c = (X_low+X_high)/2
        if (func(c) == 0.0):
            break
        if (func(c)*func(X_low) < 0):
            X_high = c
        else:
            X_low = c
            print("iteration : ","%.4f"%c)
X_low =-200
X_high = 300
bisection(X_low, X_high)


# In[ ]:




