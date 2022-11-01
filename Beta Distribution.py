"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : BETA DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment
import scipy.special as sps

#BETA DISTRIBUTION
N=100000
alpha=3.0
beta=3.0
B= np.random.beta(alpha,beta,N)

#plotting histogram:
n,bins,patches= plt.hist(B,30,density=True,color='coral',ec='r',label='Beta Distribution of 100000 \nrandom numbers')
                         
#Plotting gaussian for visualisation

plt.plot(bins, (bins**(alpha-1))*((1-bins)**(beta-1))/sps.beta(alpha,beta), lw=2, color='blue',label='Theoretical Beta distribution')
plt.title('Beta Distribution')
plt.xlabel('x $ \longrightarrow $') 
plt.ylabel('$P_{Beta}(x)$ $ \longrightarrow $')
plt.grid(True)
plt.legend()
plt.show()

# MOMENTS
K = int(input("Calculate moment upto: "))
for i in range(1,K+1):
    print("\n\t\tMoment no: ",i)
    moment_no = moment(B,moment = i)
    print("* mu",i,": ",moment_no)

#Theoretical moment
    ThMoment=0
    moment_=0
    for j in range(1,N):
        moment_ = ((B[j]-np.mean(B))**i)/N
        ThMoment+=moment_
    print("* Theoritical value: ",ThMoment)
    print( "* Error =" , moment_no-ThMoment)

# CUMULANTS
c1 = moment(B,1)
print("\n1 st cumulant ",c1)
c2 = np.mean(moment(B,2))-(np.mean(moment(B,1)))**2
print("2 nd cumulant ",c2)
c3 = np.mean(moment(B,3))-(3*(np.mean(moment(B,2))*(np.mean(moment(B,1)))))+(2*np.mean(moment(B,1)**3))
print("3 rd cumulant ",c3)
c4 = np.mean(moment(B,4))-(4*(c3)*(c1))-(3*c2**2)+(12*c2*c1**2)-(6*c1**4)
print("4 th Cumulant ",c4)
