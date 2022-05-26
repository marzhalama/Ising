import numpy as np
from sympy.utilities.iterables import multiset_permutations


sum_energy = []
n=5
v = np.ones((n), dtype=int)
x = np.ones((n), dtype=int)

for i in range(len(x)+1):
    if i>0: x[i-1] = -1
    for p in multiset_permutations(x):
        print(p)
        su = 0.0
        for d in range(len(p)):
            if d < len(p)-1:
                su += p[d]*p[d+1]*v[d]
                # print(p[d], p[d+1])
            else:
                su += p[0]*p[-1]*v[-1]
                # print(p[0], p[-1])
        sum_energy.append(su)

print(sum_energy)


    
