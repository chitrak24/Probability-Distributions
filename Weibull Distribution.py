"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : WEIBULL DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment

#WEIBULL DISTRIBUTION

lamb = 2
size = 6000
alpha = 1
W = np.random.weibull(lamb, size)

#plotting histogram:
n,bins,patches= plt.hist(W,50,density=True,color='firebrick',ec='r',label='Weibull Distribution of 6000 \n random numbers')

#plotting Weibull for visualisation
plt.plot(bins, (lamb/alpha)*(bins/alpha)**(lamb-1)*np.exp(-(bins**lamb)), linewidth=2, color='k', label= 'Theoretical Weibull Distribution')
plt.legend()
plt.grid(True)
plt.ylabel('$P_{Weibull}(x)$')
plt.show()

# MOMENTS
K = int(input("Calculate moment upto: "))
for i in range(1,K+1):
    print("\n\t\tMoment no: ",i)
    moment_no = moment(W,moment = i)
    print("* mu",i,": ",moment_no)

#Theoretical moment
    ThMoment=0
    moment_=0
    for j in range(1,size):
        moment_ = ((W[j]-np.mean(W))**i)/size
        ThMoment+=moment_
    print("* Theoritical value: ",ThMoment)
    print( "* Error =" , moment_no-ThMoment)


# CUMULANTS
c1 = moment(W,1)
print("\n1 st cumulant ",c1)
c2 = np.mean(moment(W,2))-(np.mean(moment(W,1)))**2
print("2 nd cumulant ",c2)
c3 = np.mean(moment(W,3))-(3*(np.mean(moment(W,2))*(np.mean(moment(W,1)))))+(2*np.mean(moment(W,1)**3))
print("3 rd cumulant ",c3)
c4 = np.mean(moment(W,4))-(4*(c3)*(c1))-(3*c2**2)+(12*c2*c1**2)-(6*c1**4)
print("4 th Cumulant ",c4)
