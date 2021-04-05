import sys
import numpy as np
from numpy import random as rnd



def ex_1():
    val_1 = 4+5*(2/(16+3))
    val_2 = 14**23*95**(-4)-(14**95)/(15**94)
    val_3 = (40+70-3*(40/70))*(40/70)
    val_4 = (-4*2**3-0.48)/(3**2.2*17.3)
    print("%f %f %f %f" % (val_1,val_2,val_3,val_4))

def ex_2():
    l_1 = np.arange(1,5)
    print(l_1)
    l_2 = np.arange(-4,-1.9,0.5)
    print(l_2)
    l_3 = np.arange(10,71,10)
    print(l_3)
    l_4 = np.arange(-4,54,19)
    print(l_4)
    l_5 = np.arange(100,45,-9)
    print(l_5)
    l_6 = np.arange(0,21,5)
    print(l_6)


def ex_3():
    l_1_1 = np.arange(1,6,2)
    l_1_2 = np.arange(0,7,2)
    l_1_logic = np.array_equal(l_1_1,l_1_2)
    if (l_1_logic == False) :
        print(l_1_1," e diferit de ", l_1_2)
    else:
        print(l_1_1," e la fel cu ", l_1_2)


    l_2_1 = np.arange(1,31,15)
    l_2_2 = np.arange(1,37,15)
    l_2_logic = np.array_equal(l_2_1,l_2_2)
    if (l_2_logic == False) :
        print(l_2_1," e diferit de ", l_2_2)
    else:
        print(l_2_1," e la fel cu ", l_2_2) 

    l_3_1 = np.arange(10,31,15)
    l_3_2 = np.arange(10,32,15)
    l_3_logic = np.array_equal(l_3_1,l_3_2)
    if (l_3_logic == False) :
        print(l_3_1," e diferit de ", l_3_2)
    else:
        print(l_3_1," e la fel cu ", l_3_2) 


def ex_4():
    vec = np.floor(10*rnd.rand(10))
    vec = np.sort(vec)
    min_val = vec[0]
    print(min_val)


# ex_1()
# ex_2()
# ex_3()
# ex_4()
