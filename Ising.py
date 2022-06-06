import numpy as np
from sympy.utilities.iterables import multiset_permutations
from numpy import linalg as LA

def Ising(interaction):
    sum_energy = []
    n = 4
    # interaction = np.array([1, 3, -4])
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


def Hamiltonian(interaction):
    n= 4
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

    for a in range(n+1):
        if a < a+1:
            print(a, a+1)
        else:
            print(a, 0)
    print("===================")
        
    s_1 = np.kron(Pauli_matrix_z,I)
    s_1_2 = np.kron(s_1,I)
    s_1_3 = np.kron(s_1_2,I)
    sigma_1=s_1_3
    # print(sigma_1)

    s_2 = np.kron(I,Pauli_matrix_z)
    s_2_2 = np.kron(s_2,I)
    s_2_3 = np.kron(s_2_2,I)
    sigma_2=s_2_3
    # print(sigma_2)

    s_3 = np.kron(I,I)
    s_3_2 = np.kron(s_3,Pauli_matrix_z)
    s_3_3 = np.kron(s_3_2,I)
    sigma_3=s_3_3
    # print(sigma_3)

    s_4 = np.kron(I,I)
    s_4_2 = np.kron(s_4,I)
    s_4_3 = np.kron(s_4_2,Pauli_matrix_z)
    sigma_4=s_4_3
    #print(sigma_4)

    # #print(sum)
    # print(LA.eigvals(sum))
    
if __name__ == '__main__':
    x=np.array([1, -2, 5, 2])
    Ising(x)
    # Hamiltonian(x)
    