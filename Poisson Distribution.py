"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : POISSON DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment
from scipy.special import factorial

#POISSON DISTRIBUTION

lamda = 5.0 ;
N = 100000 
P = np.random.poisson(lamda,N);

#plotting histogram:
n1,bins,patches = plt.hist(P,bins=18,density=True,color='lightgreen',ec='r',label='Poisson Distribution of 100000 \nrandom numbers')

#Plotting Poisson distribution for visualisation
plt.plot(bins,(lamda**bins * np.exp(-lamda))/ factorial(bins), linewidth=2, color='k', label='Poisson distribution (Theoretical)')
plt.title('Poisson Distribution')
plt.xlabel('x $ \longrightarrow $')
plt.ylabel('$P_{poisson}(x)$ $ \longrightarrow $')
plt.legend()
plt.xlim(-1,18)
plt.grid(True)
plt.show()

# MOMENTS
K = int(input("Calculate moment upto: "))
for i in range(1,K+1):
    print("\n\t\tMoment no: ",i)
    moment_no = moment(P,moment = i)
    print("* mu",i,": ",moment_no)

#Theoretical moment
    ThMoment=0
    moment_=0
    for j in range(1,N):
        moment_ = ((P[j]-np.mean(P))**i)/N
        ThMoment+=moment_
    print("* Theoritical value: ",ThMoment)
    print( "* Error =" , moment_no-ThMoment)

# CUMULANTS
c1 = moment(P,1)
print("\n1 st cumulant ",c1)
c2 = np.mean(moment(P,2))-(np.mean(moment(P,1)))**2
print("2 nd cumulant ",c2)
c3 = np.mean(moment(P,3))-(3*(np.mean(moment(P,2))*(np.mean(moment(P,1)))))+(2*np.mean(moment(P,1)**3))
print("3 rd cumulant ",c3)
c4 = np.mean(moment(P,4))-(4*(c3)*(c1))-(3*c2**2)+(12*c2*c1**2)-(6*c1**4)
print("4 th Cumulant ",c4)
