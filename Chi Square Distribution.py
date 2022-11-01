"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : CHI SQUARE DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment
import scipy.special as sps

#CHI SQUARE DISTRIBUTION

df, N = 20, 6000 
Chi = np.random.chisquare(df, N);

#ploting histogram
nn, bins, patches = plt.hist(Chi, 40, density=True, color='red', edgecolor='black', label='Chi square distribution of random numbers')

#plotting chi square distribution for visualisation
plt.plot(bins, bins**(df/2.0 - 1)*np.exp(-bins/2)/(2**(df/2.0)*sps.gamma(df/2.0)), linewidth=2, color='orange', label='Theoretical Chi square distribution ')
plt.legend()
plt.grid(True)
plt.show()

# MOMENTS
K = int(input("Calculate moment upto: "))
for i in range(1,K+1):
    print("\n\t\tMoment no: ",i)
    moment_no = moment(Chi,moment = i)
    print("* mu",i,": ",moment_no)

#Theoretical moment
    ThMoment=0
    moment_=0
    for j in range(1,N):
        moment_ = ((Chi[j]-np.mean(Chi))**i)/N
        ThMoment+=moment_
    print("* Theoritical value: ",ThMoment)
    print( "* Error =" , moment_no-ThMoment)


# CUMULANTS
c1 = moment(Chi,1)
print("\n1 st cumulant ",c1)
c2 = np.mean(moment(Chi))-(np.mean(moment(Chi,1)))**2
print("2 nd cumulant ",c2)
c3 = np.mean(moment(Chi,3))-(3*(np.mean(moment(Chi,2))*(np.mean(moment(Chi,1)))))+(2*np.mean(moment(Chi,1)**3))
print("3 rd cumulant ",c3)
c4 = np.mean(moment(Chi,4))-(4*(c3)*(c1))-(3*c2**2)+(12*c2*c1**2)-(6*c1**4)
print("4 th Cumulant ",c4)
