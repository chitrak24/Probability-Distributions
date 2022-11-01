"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : LAPLACE DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment

#LAPLACE DISTRIBUTION

N=100000
mu, b = 0.0, 5
L = np.random.laplace(mu,b,N)

#plotting histogram:
n,bins,patches= plt.hist(L,50,density=True,color='blue',ec='r',label='Laplace Distribution of 100000 \nrandom numbers')
                         
#Plotting gaussian for visual understanding
plt.plot(bins, np.exp(-np.abs(bins-mu)/b)/(2*b), lw=2, color='orange',label='Theoretical Laplace distribution')
plt.title('Laplace Distribution')
plt.xlabel('x $ \longrightarrow $')
plt.ylabel('$P_{Laplace}(x)$ $ \longrightarrow $')
plt.grid(True)
plt.legend()
plt.show()

# MOMENTS
K = int(input("Calculate moment upto: "))
for i in range(1,K+1):
    print("\n\t\tMoment no: ",i)
    moment_no = moment(L,moment = i)
    print("* mu",i,": ",moment_no)

#Theoretical moment
    ThMoment=0
    moment_=0
    for j in range(1,N):
        moment_ = ((L[j]-np.mean(L))**i)/N
        ThMoment+=moment_
    print("* Theoritical value: ",ThMoment)
    print( "* Error =" , moment_no-ThMoment)

# CUMULANTS
c1 = moment(L,1)
print("\n1 st cumulant ",c1)
c2 = np.mean(moment(L,2))-(np.mean(moment(L,1)))**2
print("2 nd cumulant ",c2)
c3 = np.mean(moment(L,3))-(3*(np.mean(moment(L,2))*(np.mean(moment(L,1)))))+(2*np.mean(moment(L,1)**3))
print("3 rd cumulant ",c3)
c4 = np.mean(moment(L,4))-(4*(c3)*(c1))-(3*c2**2)+(12*c2*c1**2)-(6*c1**4)
print("4 th Cumulant ",c4)


