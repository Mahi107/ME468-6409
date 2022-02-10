#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import sys
def bubblesort(n_elems):
    for n in range(len(n_elems)-1, 0, -1):
        for i in range(n):
            if n_elems[i] > n_elems[i + 1]:
                n_elems[i], n_elems[i + 1] = n_elems[i + 1], n_elems[i]

print("Unsorted list is,")
print( n_elems)
bubblesort(n_elems)
print("Sorted Array is, ")
print(n_elems)

if __name__ == "__main__":
n_elems = int(sys.argv[1:])
    do_computations(n_elems)


# In[ ]:




