#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import solve_ivp
def dSdx(x, S):
    x, v= S
    return[v, -16*v -200(x)-70]
X_0 = 0.4
v_0 = 0
S_0 = (x_0, v_0)
t = np.linspace(0, 1, 100)
sol= scipy.integrate.solve_ivp(dSdx, t_span=(0,max(t))), y0=[v0],method='Radau', t_eval=t)
x_sol = sol.T[0]
v_sol = sol.T[1]
plt.plot(t, x_sol)
plt.plot(t, v_sol)

