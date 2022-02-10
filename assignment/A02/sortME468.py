#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
def bubblesort(n_elems):
    for n in range(len(n_elems)-1, 0, -1):
        for i in range(n):
            if n_elems[i] > n_elems[i + 1]:
                n_elems[i], n_elems[i + 1] = n_elems[i + 1], n_elems[i]
n_elems = [355, 68, 222, 985, 823, 566, 708, 369, 154, 495, 605]

print("Unsorted list is,")
print( n_elems)
bubblesort(n_elems)
print("Sorted Array is, ")
print(n_elems)


# In[ ]:




