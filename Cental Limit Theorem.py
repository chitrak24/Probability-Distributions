"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : CENTRAL LIMIT THEOREM
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt

f=lambda x, m, s: 1./np.sqrt(2*np.pi*s*s)*np.exp(-(x-m)**2/(2*s*s))  #Gaussian

plt.suptitle('Uniform to Gaussian distribution using CLT')
n=1                           #Sample Size
D=np.random.uniform(-2,2,size=(10000))

mean=np.mean(D)               #Mean
std=np.std(D)/np.sqrt(n)      #Standard Deviation

plt.subplot(3,2,1)
plt.hist(D,15,density=True,color='red',edgecolor='darkorange')
plt.grid()
plt.ylabel('P(x) $\longrightarrow$')
plt.xlabel('x $\longrightarrow$')
plt.title('Sum of '+str(n)+' Variables')


plt.subplot(3,2,2)
n=2
D=np.random.uniform(-2,2,size=(n,10000))

mean=np.mean(D)
std=np.std(D)/np.sqrt(n)
D=np.mean(D,axis=0)

plt.hist(D,15,density=True,color='navy',edgecolor='crimson')
plt.grid()
plt.ylabel('P(x) $\longrightarrow$')
plt.xlabel('x $\longrightarrow$')
plt.title('Sum of '+str(n)+' Variables' )


plt.subplot(3,2,3)
n=10
D=np.random.uniform(-2,2,size=(n,10000))

mean=np.mean(D)
std=np.std(D)/np.sqrt(n)
D=np.mean(D,axis=0)

x=np.linspace(-3*std,3*std,1000)
plt.plot(x,f(x,mean,std),'k',label=r'$P(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp^{-\frac{(x-\mu)^2}{2\sigma^2}}$')
plt.hist(D,15,density=True,color='blue',edgecolor='lime')
plt.grid()
plt.ylabel('P(x) $\longrightarrow$')
plt.xlabel('x $\longrightarrow$')
plt.title('Sum of '+str(n)+' Variables' )


plt.subplot(3,2,4)
n=20
D=np.random.uniform(-2,2,size=(n,10000))

mean=np.mean(D)
std=np.std(D)/np.sqrt(n)
D=np.mean(D,axis=0)

x=np.linspace(-5*std,5*std,1000)
plt.plot(x,f(x,mean,std),'k',label=r'$P(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp^{-\frac{(x-\mu)^2}{2\sigma^2}}$')
plt.hist(D,15,density=True,color='chartreuse',edgecolor='yellow')
plt.grid()
plt.ylabel('P(x) $\longrightarrow$')
plt.xlabel('x $\longrightarrow$')
plt.title('Sum of '+str(n)+' Variables' )


plt.subplot(3,2,5)
n=40
D=np.random.uniform(-2,2,size=(n,10000))

mean=np.mean(D)
std=np.std(D)/np.sqrt(n)
D=np.mean(D,axis=0)

x=np.linspace(-10*std,10*std,1000)
plt.plot(x,f(x,mean,std),'k',label=r'$P(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp^{-\frac{(x-\mu)^2}{2\sigma^2}}$')
plt.hist(D,15,density=True,color='blueviolet',edgecolor='darkgreen')
plt.grid()
plt.ylabel('P(x) $\longrightarrow$')
plt.xlabel('x $\longrightarrow$')
plt.title('Sum of '+str(n)+' Variables' )


plt.subplot(3,2,6)
n=50
D=np.random.uniform(-2,2,size=(n,10000))

mean=np.mean(D)
std=np.std(D)/np.sqrt(n)
D=np.mean(D,axis=0)

x=np.linspace(-15*std,15*std,1000)
plt.plot(x,f(x,mean,std),'k',label=r'$P(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp^{-\frac{(x-\mu)^2}{2\sigma^2}}$')
plt.hist(D,15,density=True,color='darkgreen',edgecolor='cornflowerblue')
plt.grid()
plt.ylabel('P(x) $\longrightarrow$')
plt.xlabel('x $\longrightarrow$')
plt.title('Sum of '+str(n)+' Variables' )


plt.savefig("CLT.pdf")
plt.show()


































