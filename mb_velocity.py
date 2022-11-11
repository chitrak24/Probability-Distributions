"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Maxwell-Boltzmann Velocity DISTRIBUTION
Author       : Chitrak Roychowdhury
"""

import  numpy as np
import matplotlib.pyplot as plt

m = 28*1.66E-27
k = 1.38E-23

Temp = [100,200,300,500]

def f(v,T):
    return ((m/(2*np.pi*k*T))**(3/2))*4*np.pi*(v**2)*np.exp((-m*(v**2))/(2*k*T))


v = np.linspace(0,10000,1000000)
y= np.zeros(len(v))

for j in range(len(Temp)):
    y = f(v,Temp[j])
    plt.plot(v,y,label='T=%i'%Temp[j])
    plt.xlim(0,1000)
    plt.legend()
    plt.pause(2)


plt.xlim(0,1500)
plt.xlabel('$T$')
plt.ylabel('f(v)')
plt.grid()
plt.legend()
plt.title('Maxwell Boltzmann Velocity Distribution function')
plt.savefig('MB_Velocity.pdf')
plt.show()
