"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Radioactive Decay
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt

t_half = 10             # Half_Lifetime
alpha = np.log(2)/t_half
p = alpha                 #decay probability (success)
q = 1-p                 #survival probability(failure)

N=10000                 #initial no of atoms

def decay(N):
    population =[]
    for t in range(100):
        r = np.random.random(N)
        survival = np.sum(r<q)   #no of atoms survived
        population.append(survival)
        N = survival
    return population

mean_decay = np.mean(np.array([decay(N) for i in range(1000)]),axis=0)
std_decay = np.std(np.array([decay(N) for i in range(1000)]),axis=0)

T=range(100)
exact = N*np.exp(-alpha*T)
plt.subplot(1,2,1)
plt.plot(T,mean_decay,'-',c='g',label='Mean Decay')
plt.plot(T,exact,'o',c='b',label=r'$\frac{dN}{dt}=-\alpha t$')
plt.legend()
plt.grid()

plt.subplot(1,2,2)
plt.plot(T,std_decay**2/mean_decay,'--',c='r',label='Fluctuations')
plt.legend()
plt.grid()

plt.savefig('decay.pdf')
plt.show()

