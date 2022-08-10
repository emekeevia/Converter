import matplotlib.pyplot as plt
import numpy as np
import scipy.io as spio
import math as math
import mat73
import h5py
from matplotlib import cm
from threading import Thread
from scipy.interpolate import interp1d


#data = spio.loadmat('../Загрузки/E2_10001_STD_L0_F285.000.mat')
#f = h5py.File('../Загрузки/E2_10001_STD_L0_F285.000.mat', 'r')
#Raw_data = f['Raw_data']
#Raw_data = np.array(Raw_data)
#Raw_data = np.transpose(Raw_data)

def reading(i):
    fw = open("../CLionProjects/SAR_CPP/E2_10001_STD_L0_F285_for_cpp_"+ str(i)+"_part.txt", 'w')
    for j in range(int(i*len(Raw_data)/4), int((i+1)*len(Raw_data)/4)):
        num = [str(i).replace(' ','') for i in Raw_data[j]]
        str_num = " ".join(num)
        str_num = str_num + '\n'
        fw.write(str_num)
        print(str(j))
    fw.close()

for i in range(2):
    th = Thread(target=reading, args=(i+2, ))
    th.start()


'''
fw = open("../CLionProjects/SAR_CPP/E2_10001_STD_L0_F285_for_cpp_s_part.txt", 'w')
for j in range(int(len(Raw_data[0])/2), len(Raw_data[0])):
    num = [str(i).replace(' ','') for i in Raw_data[:,j]]
    str_num = " ".join(num)
    str_num = str_num + '\n'
    fw.write(str_num)
    print(str(j))
fw.close()
'''
#print("All done!")
#f.close()