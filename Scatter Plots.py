"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Scatter Plots
Author       : Chitrak Roychowdhury
"""


import numpy as np
import matplotlib.pyplot as plt

N=10000   #total no. of entries to be generated in arrays

#generating array of random numbers from various distribution
a=np.random.normal(0,1,N)    #normal distribution
b=np.random.exponential(1,N)    #exponential distribution
c=np.random.poisson(3.0,N)    #poisson distribution
d=np.random.uniform(0,1,N)   #uniform distribution
e=np.random.rayleigh(1,N)   #rayleigh distribution
f=np.random.pareto(3.0,N)   #pareto distribution

a1=a[1::2]   #odd entries of a
a2=a[::2]     #even entries of a
b1=b[1::2]   #odd entries of b
b2=b[::2]      #even entries of b
c1=c[1::2]     #odd entries of c
c2=c[::2]       #even entries of c
d1=d[1::2]    #odd entries of d
d2=d[::2]      #even entries of d
e1=e[1::2]    #odd entries of e
e2=e[::2]      #even entries of e
f1=f[1::2]    #odd entries of f
f2=f[::2]      #even entries of f
          
#scatter plots of random numbers from different distributions
plt.suptitle('Scatter plot of random numbers from different distribution')
plt.subplot(3,2,1)
plt.scatter(a1,a2,c='cyan',label='for random numbers from normal distribution')
plt.legend(loc='best')
plt.xlabel('odd entries $\longrightarrow$')
plt.ylabel('even entries $\longrightarrow$')
plt.grid(True)

plt.subplot(3,2,2)
plt.scatter(b1,b2,c='darkblue',label='for random numbers from exponential distribution')
plt.legend(loc='best')
plt.xlabel('odd entries $\longrightarrow$')
plt.ylabel('even entries $\longrightarrow$')
plt.grid(True)

plt.subplot(3,2,3)
plt.scatter(c1,c2,c='red',label='for random numbers from poisson distribution')
plt.legend(loc='best')
plt.xlabel('odd entries $\longrightarrow$')
plt.ylabel('even entries $\longrightarrow$')
plt.grid(True)

plt.subplot(3,2,4)
plt.scatter(d1,d2,c='darkgreen',label='for random numbers from uniform distribution')
plt.legend(loc='best')
plt.xlabel('odd entries $\longrightarrow$')
plt.ylabel('even entries $\longrightarrow$')
plt.grid(True)

plt.suptitle('Scatter plot of random numbers from different distribution')
plt.subplot(3,2,5)
plt.scatter(e1,e2,c='magenta',label='for random numbers from Rayleigh distribution')
plt.legend(loc='best')
plt.xlabel('odd entries $\longrightarrow$')
plt.ylabel('even entries $\longrightarrow$')
plt.grid(True)

plt.suptitle('Scatter plot of random numbers from different distribution')
plt.subplot(3,2,6)
plt.scatter(f1,f2,c='yellow',label='for random numbers from pareto distribution')
plt.legend(loc='best')
plt.xlabel('odd entries $\longrightarrow$')
plt.ylabel('even entries $\longrightarrow$')
plt.grid(True)

plt.show()
plt.savefig('scatter_plot.pdf')
