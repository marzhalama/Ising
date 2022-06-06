import numpy as np
from sympy.utilities.iterables import multiset_permutations


sum_energy = []
n = 6
interaction = np.ones((n), dtype=int)
set_of_configuration = np.ones((n), dtype=int)
temp_min_energy = 30.0
temp_set = np.array([])


for i in range(n+1):
    if i>0: set_of_configuration[i-1] = -1
    for p in multiset_permutations(set_of_configuration):
        print(p)
        su = 0.0
        for d in range(len(p)):
            if d < len(p)-1:
                su += p[d]*p[d+1]*interaction[d]
                # print(p[d], p[d+1])
            else:
                su += p[0]*p[-1]*interaction[-1]
                # print(p[0], p[-1])
        if temp_min_energy > su:
            temp_min_energy = su 
            temp_set = p
        
        sum_energy.append(su)
    

print(sum_energy)
print(temp_min_energy, temp_set)
    
