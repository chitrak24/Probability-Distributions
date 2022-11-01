"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : GAUSSIAN DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment

#GAUSSIAN DISTRIBUTION

mu = 0.0    #Mean
sigma = 10  #Standard Deviation

#No of points
M = 30000   
nbins = 40

y= np.random.normal(mu,sigma,M)

#plotting histogram:

n,bins,patches= plt.hist(y,nbins, density='True', color='black', ec='r', label='Distribution curve of 30000 \nrandom numbers')

#plotting gaussian for visualisation
gaussian = 1/(np.sqrt(2*np.pi*sigma**2)) *np.exp(-(bins-mu)**2/(2*sigma**2))
plt.plot(bins, gaussian ,linewidth=2, color='cyan', label='Theoretical gaussian curve')
plt.title('Gaussian Distribution')
plt.xlabel('x $ \longrightarrow $')
plt.ylabel('$N_{Gaussian}(x)$ $ \longrightarrow $')
plt.grid('True')
plt.legend()
plt.show()

# MOMENTS
K = int(input("Calculate moment upto: "))
for i in range(1,K+1):
    print("\n\t\tMoment no: ",i)
    moment_no = moment(y,moment = i)
    print("* mu",i,": ",moment_no)

#Theoretical moment
    ThMoment=0
    moment_=0
    for j in range(1,M):
        moment_ = ((y[j]-np.mean(y))**i)/M
        ThMoment+=moment_
    print("* Theoritical value: ",ThMoment)
    print( "* Error =" , moment_no-ThMoment)

# CUMULANTS
c1 = moment(y,1)
print("\n1 st cumulant ",c1)
c2 = np.mean(moment(y,2))-(np.mean(moment(y,1)))**2
print("2 nd cumulant ",c2)
c3 = np.mean(moment(y,3))-(3*(np.mean(moment(y,2))*(np.mean(moment(y,1)))))+(2*np.mean(moment(y,1)**3))
print("3 rd cumulant ",c3)
c4 = np.mean(moment(y,4))-(4*(c3)*(c1))-(3*c2**2)+(12*c2*c1**2)-(6*c1**4)
print("4 th Cumulant ",c4)





