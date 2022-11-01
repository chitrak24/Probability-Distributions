"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : GAMMA DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment
import scipy.special as sps

#GAMMA DISTRIBUTION

shape=6000
scale=2
size=2
G= np.random.gamma(scale,size,shape)

#plotting histogram:
n, bins, patches = plt.hist(G, 50, density=True, color='yellow', edgecolor='brown', label='Gamma Function of 6000 random numbers')

#plotting gamma for visualisation
plt.plot(bins, bins**(scale-1)*(np.exp(-bins/size)/(sps.gamma(scale)*size**scale)), linewidth=2, color='r', label='Theoretical Gamma Distribution')
plt.legend(loc='best')
plt.xlim(0,25)
plt.ylim(0,0.2)
plt.grid(True)
plt.ylabel('$P_{\Gamma}(x)$')
plt.show()

# MOMENTS
K = int(input("Calculate moment upto: "))
for i in range(1,K+1):
    print("\n\t\tMoment no: ",i)
    moment_no = moment(G,moment = i)
    print("* mu",i,": ",moment_no)

#Theoretical moment
    ThMoment=0
    moment_=0
    for j in range(1,shape):
        moment_ = ((G[j]-np.mean(G))**i)/shape
        ThMoment+=moment_
    print("* Theoritical value: ",ThMoment)
    print( "* Error =" , moment_no-ThMoment)

# CUMULANTS
c1 = moment(G,1)
print("\n1 st cumulant ",c1)
c2 = np.mean(moment(G,2))-(np.mean(moment(G,1)))**2
print("2 nd cumulant ",c2)
c3 = np.mean(moment(G,3))-(3*(np.mean(moment(G,2))*(np.mean(moment(G,1)))))+(2*np.mean(moment(G,1)**3))
print("3 rd cumulant ",c3)
c4 = np.mean(moment(G,4))-(4*(c3)*(c1))-(3*c2**2)+(12*c2*c1**2)-(6*c1**4)
print("4 th Cumulant ",c4)

