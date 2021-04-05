import sys
import numpy as np
from numpy import random as rnd
import scipy.io as sio

def ex_1():
    vec_1 = np.floor(40+80*rnd.rand(30))
    vec_2 = np.where( (vec_1 > 50) & (vec_1 < 70) )
    pos = vec_2[0]
    print(pos)
    sio.savemat("P_vec.mat",{"pos":pos})

def ex_2():
    a_vec = [2, 4, -5, 7, 18, 0]
    a_vec_flip = np.flip(a_vec)
    print(a_vec_flip)

def ex_3():
    b_vec = np.floor(5+10*rnd.rand(rnd.randint(1,20)))
    b_vec_imp = b_vec[1::2] #presupunand ca prima pozitie impara este 1, iar elementul de pe indexul 0 este pe o pozitie para
    print(b_vec_imp)

def ex_4():
    A_mat = np.floor(10+10*rnd.rand(10,10))
    A_vec_5by5 = A_mat[5::,5::]
    print(A_vec_5by5)

def ex_5():
    c_vec = np.array([8, 9, 7, 4, 5, 2, 6, 5, 4, 1, 3, 9, 8, 7, 5, 2, 3])
    c_vec_pos = np.where( (c_vec > 2) & (c_vec < 5) )
    pos = c_vec_pos[0]
    c_new_vec = [c_vec[x] for x in pos]
    print(c_new_vec)

def ex_6(mat):
    print(mat)
    sec_diag = np.diag(np.rot90(mat))
    print("diagonala secundara: ",sec_diag)
    mat_triungh_sup = np.triu(mat)
    print("matricea superior triunghiulara: \n",mat_triungh_sup)
    mat_triungh_inf = np.tril(mat)
    print("matricea inferior triunghiulara: \n",mat_triungh_inf)

    vec = [sec_diag,mat_triungh_sup,mat_triungh_inf]
    return vec


def ex_7():
    A = np.array([8, 9, 10, 11])
    B = np.array([5])
    C = np.array([9, 8, 5])

    lengths = np.array([len(A),len(B),len(C)])
    MAT = np.zeros((3,np.max(lengths)))

    to_add = np.max(lengths) - lengths
    


    for i in range(to_add[0]):
        A = np.hstack( (A,0) )
    for i in range(to_add[1]):
        B = np.hstack( (B,0) )
    for i in range(to_add[2]):
        C = np.hstack( (C,0) )

    
    MAT = np.vstack( (A,B,C) )
    for i in range(3):
        MAT[i][0::] = np.roll(MAT[i][0::],to_add[i])
    
    print(MAT)
    
def ex_8():
    MAT = np.zeros((3,7))
    MAT[0][0::] = np.linspace(1,7,7)
    MAT[1][0::] = np.linspace(9,-3,7)
    MAT[2][0::] = 2**np.linspace(2,8,7)

    print(MAT)

# ex_1()
# ex_2()
# ex_3()
# ex_4()
# ex_5()

# mat = np.floor(10+10*rnd.rand(10,10))
# v = ex_6(mat)

# ex_7()
# ex_8()