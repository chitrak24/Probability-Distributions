"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Monte Carlo Integration
Author       : Chitrak Roychowdhury
"""

import numpy as np

N=10000 #no of random points
a,b=0,np.pi
x=np.random.uniform(a,b,N) #generation of points
f=lambda x:np.sin(x) #function

MC_value=(b-a)*np.mean(f(x))
print(MC_value)

#error
err=lambda N:np.std(f(x))/np.sqrt(N)
print(err(10000))


###################################

def MCI(f,a,b):
	N=10000
	x=np.random.uniform(a,b,N)
	return (b-a)*np.mean(f(x))
	

f=lambda x:np.sin(x)
a,b=0,np.pi
val=MCI(f,a,b)
print(val)

#distribution
import matplotlib.pyplot as plt
X=[MCI(f,a,b) for i in range(10000)]
with plt.xkcd():
	plt.hist(X,bins=40,color='b',ec='r')
	plt.show()
	

#################################
#MC double integral 1-x2-y2

import numpy as np

def MCI(f,a,b,c,d): 
	N=10000
	x=np.random.uniform(a,b,N)
	y=np.random.uniform(c,d,N)
	return np.mean(f(x,y))
	
f=lambda x,y:1-x**2-y**2

a,b,c,d=0,1,0,1
MCval=MCI(f,a,b,c,d)
print(MCval)

#plot of results
import matplotlib.pyplot as plt
X=[MCI(f,a,b,c,d) for i in range(10000)]
with plt.xkcd():
	plt.hist(X,bins=40,color='red',ec='yellow')
	plt.show()


#################################
# Estimation of Pi

import numpy as np
x=np.random.uniform(-1,1,1000)
y=np.random.uniform(-1,1,1000)
z=x**2+y**2<1   #array contains boolean true and false
pi=4*sum(z)/1000  #sum(z) is sum of True=1 and False=0
print('pi = ',pi)
