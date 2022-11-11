"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Maxwell-Boltzmann DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import  numpy as np
import matplotlib.pyplot as plt

mu = 7.1
k = 8.6E-5

Temp = [100,200,300,500]

def f(e,T):
    return 1/(np.exp((e-mu)/(k*T)))


E = np.linspace(0,10,5000)
y= np.zeros(len(E))

for j in range(len(Temp)):
    y = f(E,Temp[j])
    plt.plot(E,y,label='T=%i'%Temp[j])
    plt.legend()
    plt.pause(2)

plt.xlim(7.00,7.35)
plt.ylim(0,1)
plt.xlabel('$E$eV')
plt.ylabel('f(E)')
plt.grid(True)
plt.legend()
plt.title('Maxwell Boltzmann Distribution function')
plt.savefig('MB.pdf')
plt.show()
