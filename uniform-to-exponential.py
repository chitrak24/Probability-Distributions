"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Exponential Variate from Uniform Variate
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt

N=100000
u = np.random.uniform(0,1,N)

x = -np.log(1-u)   #Inverse Transformation

v,bins,patches = plt.hist(x,50,ec='red',color='blue',label=r'$P(x) = {\lambda}e^{-{\lambda}x}$')

bin_mid = ( bins[1:] + bins[:-1] )* 0.5
bin_width = bins[1] - bins[0]
exp_dist = N * np.exp(-bin_mid) * bin_width

plt.plot(bin_mid, exp_dist,'-o',color='red',label='exponential distribution')
plt.grid()
plt.legend()
plt.title('Uniform Variate $\longrightarrow$ Exponential Variate')
plt.savefig("uni_to_exp.pdf")
plt.show()
