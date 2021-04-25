import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from numpy import random as rnd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator
from matplotlib.colors import LinearSegmentedColormap,ListedColormap
import matplotlib.colors
from matplotlib import cm



#subiectul 2#
#def s2_function(M_in):
    # M_out = np.zeros((4,3))
    
    # sz = np.shape(M_in)
    # nr_lin = sz[0]
    # nr_col = sz[1]

    # M1 = M_in[0:3,0:3]
    # M_out[0,:] = np.diag(np.rot90(M1))

    # M2 = M_in[0:3,nr_col-3:nr_col]
    # M_out[1,:] = np.diag(M2)

    # M3 = M_in[nr_lin-3:nr_lin,0:3]
    # M_out[2,:] = np.diag(M3)

    # M4 = M_in[nr_lin-3:nr_lin,nr_col-3:nr_col]
    # M_out[3,:] = np.diag(np.rot90(M4))

    # return M_out
#def s2_script(M_out):
    # plt.close("all")
    # gs = gridspec.GridSpec(4,2)
    # plt.figure(1)
    # plt.suptitle("da")

    # sbl1 = plt.subplot(gs[:,0])
    # sbl1.plot(np.transpose(M_out))
    # plt.title("Intreaga Matrice")
    
    # sbl2 = plt.subplot(gs[0,1])
    # sbl2.plot(M_out[0,:])
    # plt.title("Prima linie")

    # sbl3 = plt.subplot(gs[1,1])
    # sbl3.plot(M_out[1,:])
    # plt.title("A doua linie")

    # sbl4 = plt.subplot(gs[2,1])
    # sbl4.plot(M_out[2,:])
    # plt.title("A treia linie")

    # sbl5 = plt.subplot(gs[3,1])
    # sbl5.plot(M_out[3,:])
    # plt.title("A patra linie")

    # plt.tight_layout()
    # plt.show()
#M_in = np.floor(10+10*(rnd.rand(rnd.randint(5,10),rnd.randint(5,10))))
#print(M_in)
#M_out = s2_function(M_in)
#print(M_out)
#s2_script(M_out)
#...............#



#subiectul 3#
#def s3_script():
    # plt.close("all")
    # nr_lin = 3
    # nr_col = 4

    # M = rnd.randn(nr_lin,nr_col)
    # M = 2+np.floor(np.abs(M))
    # print(M)
    
    # new_inferno = cm.get_cmap('inferno',2)

    # X = np.arange(0,3)
    # Y = np.arange(0,4)
    # X,Y = np.meshgrid(X,Y)
    # Z = M[X,Y]
    
    # fig = plt.figure()
    # ax = fig.add_subplot(111,projection='3d')
    # gr = ax.plot_surface(X,Y,Z,cmap=new_inferno)
    # ax.set_ylabel("y")
    # ax.set_zlabel("z")
    # ax.set_xlabel("x")
    # ax.view_init(0,0)

    # plt.colorbar(gr)
    # plt.show()
#s3_script()#
#..............#



#subiectul 5#
# def s5_script():
    # nr_lin = 13
    # nr_col = 50
    # M = np.round(10+10*rnd.rand(nr_lin,nr_col),2)
    # while(len(np.unique(M[nr_lin-1,:])) - len(M[nr_lin-1,:]) !=0 ):
    #     M = np.round(10+10*rnd.rand(nr_lin,nr_col),2)
    # return M
# def s5_function(M):
    # plt.close("all")
    # gs = gridspec.GridSpec(7,3)
    # plt.figure(1)
    # plt.suptitle("Matricea M")

    # sbl1 = plt.subplot(gs[0:2,0])
    # sbl1.plot(M[0,:])
    # plt.title("Prima linie")
    # sbl2 = plt.subplot(gs[0:2,1])
    # sbl2.plot(M[1,:])
    # plt.title("A doua linie")
    # sbl3 = plt.subplot(gs[0:2,2])
    # sbl3.plot(M[2,:])
    # plt.title("A treia linie")

    # sbl4 = plt.subplot(gs[2:4,0])
    # sbl4.plot(M[3,:])
    # plt.title("A patra linie")
    # sbl5 = plt.subplot(gs[2:4,1])
    # sbl5.plot(M[4,:])
    # plt.title("A cincea linie")
    # sbl6 = plt.subplot(gs[2:4,2])
    # sbl6.plot(M[5,:])
    # plt.title("A sasea linie")

    # sbl7 = plt.subplot(gs[4,0])
    # sbl7.plot(M[6,:])
    # plt.title("A saptea linie")
    # sbl8 = plt.subplot(gs[5,0])
    # sbl8.plot(M[7,:])
    # plt.title("A opta linie")
    # sbl9 = plt.subplot(gs[6,0])
    # sbl9.plot(M[8,:])
    # plt.title("A noua linie")

    # sbl10 = plt.subplot(gs[4,2])
    # sbl10.plot(M[9,:])
    # plt.title("A zecea linie")
    # sbl11 = plt.subplot(gs[5,2])
    # sbl11.plot(M[10,:])
    # plt.title("A unspea linie")
    # sbl12 = plt.subplot(gs[6,2])
    # sbl12.plot(M[11,:])
    # plt.title("A doispea linie")

    # sbl13 = plt.subplot(gs[4:7,1])
    # sbl13.plot(M[12,:])
    # plt.title("A treispea linie")

    # plt.tight_layout()
    # plt.show()
# M = s5_script()
# s5_function(M)
# ....................#



#subiectul 7#
# def s7_function():
    # m=100
    # phi = np.arange(0,2*np.pi,(2*np.pi)/m)
    # v1 = np.cos(phi)
    # v2 = np.sin(phi)


    # M = np.zeros((m,50))
    # for i in range(m):
    #     M[i,:] = np.linspace(v1[i],v2[i],50)
    # return (v1,v2,M)
# def s7_script():
    # ret_val = s7_function()
    # M = ret_val[2]
    # m = ret_val[0]
    # m = len(m)
    # plt.close("all")

    # plt.figure(1)
    # plt.title("liniile pare")
    # for i in range(0,m,2):
    #     plt.plot(M[i,:])

    # plt.figure(2)
    # plt.title("liniile impare")
    # for i in range(1,m,2):
    #     plt.plot(M[i,:])
    # plt.show()
# s7_script()
# ...................#



#subiectul 8#
# def s8_script():
    # nr = 10
    # num = np.arange(1,nr+1,1)
    # v1 = np.cumsum(num)
    # v2 = np.cumprod(num)
    # print(v1,v2,sep = "\n")

    # v = v1/v2

    # plt.close("all")

    # plt.figure(1)
    # plt.plot(v)
    # plt.stem(np.arange(0,nr),v,'r')
    # plt.step(np.arange(0,nr),v,'g-.')
    # plt.show()
# s8_script()
#..................#



#subiectul 10#
# def s10_function():
    # a = rnd.randint(10,30) 
    # b = rnd.randint(10,30)
    # M = np.floor(1000*rnd.rand(a,b) - 500)

    # nr_col = 0
    # for i in range(b):
    #     cur_len = len(np.unique(M[:,i]))
    #     if(cur_len != a):
    #         nr_col+=1
    # return M
# def s10_script():
    # M = s10_function()
    # nr_lin = np.shape(M)[0]
    # print(nr_lin)
    # plt.close("all")


    # if(nr_lin % 4 == 0):
        # it = int(nr_lin / 4)
        # gs = gridspec.GridSpec(it,4)
        # plt.figure(1)
        # plt.suptitle("%d linii" %nr_lin)
        # for i in range(0,nr_lin):
        #     sbl = plt.subplot(gs[int(np.floor(i/4)),i%4])
        #     sbl.plot(M[i,:])
        # plt.show()

    # elif(nr_lin % 4 == 1):
        # four_mult = nr_lin - 9
        # four_mult_it = int(four_mult / 4)
        # gs = gridspec.GridSpec(four_mult_it + 3,4)
        # plt.figure(2)
        # plt.suptitle("%d linii" %nr_lin)

        # temp_i=0
        # for i in range(0,four_mult):
        #     sbl = plt.subplot(gs[int(i/4),i%4])
        #     sbl.plot(M[i,:])
        #     temp_i = i
        # sbl = plt.subplot(gs[four_mult_it:four_mult_it+3,0])
        # sbl.plot(M[temp_i+1,:])
        # temp_i = temp_i+2

        # sbl = plt.subplot(gs[four_mult_it:four_mult_it+2,1])
        # sbl.plot(M[temp_i,:])
        # temp_i += 1

        # sbl = plt.subplot(gs[four_mult_it+2,1])
        # sbl.plot(M[temp_i,:])
        # temp_i += 1

        # for i in range(3):
        #     sbl = plt.subplot(gs[four_mult_it+i,2])
        #     sbl.plot(M[temp_i,:])
        #     temp_i += 1
        # for i in range(3):
        #     sbl = plt.subplot(gs[four_mult_it+i,3])
        #     sbl.plot(M[temp_i,:])
        #     temp_i += 1

        # plt.show()

    # elif(nr_lin % 4 == 2):
        # four_mult = nr_lin - 6
        # four_mult_it = int(four_mult / 4)
        # gs = gridspec.GridSpec(four_mult_it+3,4)
        # plt.figure(3)
        # plt.suptitle("%d linii" %nr_lin)

        # temp_i = 0
        # for i in range(0,four_mult):
        #     sbl = plt.subplot(gs[int(i/4),i%4])
        #     sbl.plot(M[i,:])
        #     temp_i = i
        # temp_i += 1
        # for i in range(3):
        #     sbl = plt.subplot(gs[four_mult_it:four_mult_it+3,i])
        #     sbl.plot(M[temp_i,:])
        #     temp_i = i
        # temp_i += 1
        # for i in range(3):
        #     sbl = plt.subplot(gs[four_mult_it+i,3])
        #     sbl.plot(M[temp_i + i,:])
        # plt.show()

    # else:
        # four_mult = nr_lin - 7
        # four_mult_it = int(four_mult / 4)
        # gs = gridspec.GridSpec(four_mult_it+3,4)
        # plt.figure(4)
        # plt.suptitle("%d linii" %nr_lin)

        # temp_i = 0
        # for i in range(0,four_mult):
        #     sbl = plt.subplot(gs[int(i/4),i%4])
        #     sbl.plot(M[i,:])
        #     temp_i = i
        # temp_i += 1
        # sbl = plt.subplot(gs[four_mult_it:four_mult_it+3,0])
        # sbl.plot(M[temp_i,:])
        # temp_i += 1

        # for i in range(3):
        #     sbl = plt.subplot(gs[four_mult_it:four_mult_it+2,i+1])
        #     sbl.plot(M[temp_i,:])
        #     temp_i = i
        # temp_i += 1
        # for i in range(3):
        #     sbl = plt.subplot(gs[four_mult_it+2,i+1])
        #     sbl.plot(M[temp_i+i,:])
        


        # plt.show()
# s10_script()
#......................#
