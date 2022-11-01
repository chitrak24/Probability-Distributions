"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : RAYLEIGH DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment

#RAYLEIGH DISTRIBUTION

sigma, N = 3.0, 6000
R = np.random.rayleigh(sigma, N);

#plotting histogram
n, bins, patches = plt.hist(R, 'fd', density=True, color='orchid', ec='crimson', label='Rayleigh Distribution of random 6000 numbers')

#plotting Rayleigh distribution for visualisation
plt.plot(bins, bins*np.exp(-(bins**2)/(2*sigma**2))/(sigma**2), linewidth=2, color='r', label='Theoretical Rayleigh Distribution')
plt.legend()
plt.grid(True)
plt.ylabel('$P_{Rayleigh}(x)$')
plt.show()

# MOMENTS
K = int(input("Calculate moment upto: "))
for i in range(1,K+1):
    print("\n\t\tMoment no: ",i)
    moment_no = moment(R,moment = i)
    print("* mu",i,": ",moment_no)

#Theoretical moment
    ThMoment=0
    moment_=0
    for j in range(1,N):
        moment_ = ((R[j]-np.mean(R))**i)/N
        ThMoment+=moment_
    print("* Theoritical value: ",ThMoment)
    print( "* Error =" , moment_no-ThMoment)

# CUMULANTS
c1 = moment(R,1)
print("\n1 st cumulant ",c1)
c2 = np.mean(moment(R))-(np.mean(moment(R,1)))**2
print("2 nd cumulant ",c2)
c3 = np.mean(moment(R,3))-(3*(np.mean(moment(R,2))*(np.mean(moment(R,1)))))+(2*np.mean(moment(R,1)**3))
print("3 rd cumulant ",c3)
c4 = np.mean(moment(R,4))-(4*(c3)*(c1))-(3*c2**2)+(12*c2*c1**2)-(6*c1**4)
print("4 th Cumulant ",c4)
