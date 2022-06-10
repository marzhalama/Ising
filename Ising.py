from code import interact
import weakref
import numpy as np
from sympy.utilities.iterables import multiset_permutations
from numpy import linalg as LA
from itertools import product
from scipy.linalg import toeplitz




def ising_energy(interaction, n):
    sum_energy = []
    set_of_configuration = np.ones((n), dtype=int)
    temp_min_energy = 30.0
    temp_set = np.array([])


    for i in range(n+1):
        if i>0: set_of_configuration[i-1] = -1
        for p in multiset_permutations(set_of_configuration):
            # print(p)
            su = 0.0
            for d in range(len(p)):
                if d < len(p)-1:
                    su += p[d]*p[d+1]*interaction[d,d+1]
                    # print(p[d], p[d+1], interaction[d][d+1])
                else:
                    su += p[0]*p[-1]*0
                    # print(p[0], p[-1])
            if temp_min_energy > su:
                temp_min_energy = su 
                temp_set = p
            
            sum_energy.append(su)
        

    print("The spectrum of allowed energy levels of the system:",sum_energy, "\n")
    print("Min energy:", temp_min_energy, "of the eigenvectors:", temp_set , "\n")


def Hamiltonian(interaction, n):
    Pauli_matrix_z=np.array(([1,0],[0,-1]))
    I=np.array(([1,0], [0,1]))

    
    all_matrix = []
    for outside in range(n):
        line_matrix = np.array([])
        for inside in range(n):
            if inside == 0 and outside == 0:
                line_matrix = Pauli_matrix_z
            elif inside == 0 and outside > 0:
                line_matrix = I
            elif inside == outside:
                line_matrix = np.kron(line_matrix, Pauli_matrix_z)
            else:
                line_matrix = np.kron(line_matrix, I)
        
        all_matrix.append(line_matrix)
       
    Ha = None
    for a in range(n):
        # print(all_matrix[a], "\n\n")
        if a < n-1:
            tmp = all_matrix[a] * all_matrix[a+1] * interaction[a][a+1]
            if Ha is None:
                Ha = tmp
            else:
                Ha += tmp
        else:
            Ha += all_matrix[a] * all_matrix[0] * 0 
    # print(Ha)
    print("The set of eigenvalues:", LA.eigvals(Ha))

    
if __name__ == '__main__':
    n = 4
    vector_of_inetacrtion = np.array([-2, -2, 1, -2])
    interaction=toeplitz(vector_of_inetacrtion)
    # print(toeplitz(vector_of_inetacrtion))
    ising_energy(interaction, n)
    # Hamiltonian(interaction, n)
    # for x in product([-1,1], repeat = n):
    #     print(x)
    # for x in range(4):
    #     b = format(x, "03b")
    #     s = [int(i)*2 - 1 for i in b]
    #     print(s[0])
    # arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    # print(arr[0, 1, 2]) 
            
