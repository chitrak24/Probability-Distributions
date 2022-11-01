"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : BINOMIAL DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
from scipy.stats import moment

#BINOMIAL DISTRIBUTION

n = 20  #no of trials
p = 0.6 #success probability
pts = 20000 #no of points

N = np.random.binomial(n, p, pts)

#ploting histogram
m,bins,patches= plt.hist(N,'sturges',density=True, color='red', ec='b', label='Binomial Distribution curve of 20000 \nrandom numbers')
                          
#Plotting binomial curve for visualisation
plt.plot(bins, comb(n,bins)*pow(p,bins)*pow(1-p,n-bins), linewidth=2, color='yellow',label='Theoretical Binomial distribution')
plt.title('Binomial Distribution')
plt.xlabel('x $ \longrightarrow $')
plt.ylabel('$P_{Binomial}(x)$ $ \longrightarrow $')
plt.grid(True)
plt.legend()
plt.show()

# MOMENTS
K = int(input("Calculate moment upto: "))
for i in range(1,K+1):
    print("\n\t\tMoment no: ",i)
    moment_no = moment(N,moment = i)
    print("* mu",i,": ",moment_no)

#Theoretical moment
    ThMoment=0
    moment_=0
    for j in range(1,pts):
        moment_ = ((N[j]-np.mean(N))**i)/pts
        ThMoment+=moment_
    print("* Theoritical value: ",ThMoment)
    print( "* Error =" , moment_no-ThMoment)


# CUMULANTS
c1 = moment(N,1)
print("\n1 st cumulant ",c1)
c2 = np.mean(moment(N,2))-(np.mean(moment(N,1)))**2
print("2 nd cumulant ",c2)
c3 = np.mean(moment(N,3))-(3*(np.mean(moment(N,2))*(np.mean(moment(N,1)))))+(2*np.mean(moment(N,1)**3))
print("3 rd cumulant ",c3)
c4 = np.mean(moment(N,4))-(4*(c3)*(c1))-(3*c2**2)+(12*c2*c1**2)-(6*c1**4)
print("4 th Cumulant ",c4)
