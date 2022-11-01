"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : EXPONENTIAL DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment

#EXPONENTIAL DISTRIBUTION

beta = 20  #rate parameter
N = 100000 #no of points

E=np.random.exponential(beta,N)

#plotting histogram
n,bins,patches = plt.hist(E, 20, density='True', color='orange', ec='r', label='Exponential Distribution of 100000 \n random numbers')

#plotting exponential curve for visualisation
expf = 1/beta*np.exp(-bins/beta)
plt.plot(bins,expf,linewidth=2, color='magenta',label='Theoretical Exponential distribution')
plt.title("Exponential Distribution")
plt.xlabel('x $ \longrightarrow $')
plt.xlim(0,150)
plt.ylabel('$P_{Exponential}(x)$ $ \longrightarrow $')
plt.grid(True)
plt.legend()
plt.show()

# MOMENTS
K = int(input("Calculate moment upto: "))
for i in range(1,K+1):
    print("\n\t\tMoment no: ",i)
    moment_no = moment(E,moment = i)
    print("* mu",i,": ",moment_no)

#Theoretical moment
    ThMoment=0
    moment_=0
    for j in range(1,N):
        moment_ = ((E[j]-np.mean(E))**i)/N
        ThMoment+=moment_
    print("* Theoritical value: ",ThMoment)
    print( "* Error =" , moment_no-ThMoment)

# CUMULANTS
c1 = moment(E,1)
print("\n1 st cumulant ",c1)
c2 = np.mean(moment(E,2))-(np.mean(moment(E,1)))**2
print("2 nd cumulant ",c2)
c3 = np.mean(moment(E,3))-(3*(np.mean(moment(E,2))*(np.mean(moment(E,1)))))+(2*np.mean(moment(E,1)**3))
print("3 rd cumulant ",c3)
c4 = np.mean(moment(E,4))-(4*(c3)*(c1))-(3*c2**2)+(12*c2*c1**2)-(6*c1**4)
print("4 th Cumulant ",c4)
