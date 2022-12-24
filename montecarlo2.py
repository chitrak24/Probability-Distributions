"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Monte Carlo Integration
Author       : Chitrak Roychowdhury
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps


##Error Function Integration
f=lambda z: 2/np.pi**.5 *np.exp(-z**2)  #function to integrate
a, b=0, 2*np.pi                         #x Limits
N= 10000                               #No. of random points projected
x=np.linspace(a,b,10000)                 

y_min, y_max= 0, np.max((f(x)))+1       #y Limits
A=(b-a)*(y_max-y_min)                   #Area of total random limit

X= np.random.uniform(a, b, N)           
Y= np.random.uniform(y_min, y_max, N)   
n=np.sum([abs(Y)<=abs(f(X))])           #Dots inside the function

plt.scatter(X, Y, c='r', s=.5, antialiased=False)
plt.plot(x, f(x), c='blue',label='f(x)')
plt.grid()
plt.xlabel(r'X$\longrightarrow$')
plt.ylabel(r'Y$\longrightarrow$')
plt.title('Error Function Integration Monte Carlo Method')
plt.show()

Int=(b-a)*np.mean(f(X))
Int2=A*n/N

print('\n Error Function Integration')
print('Integration by Monte Carlo Method(Functional):',Int)
print('Integration by Monte Carlo Method(Dot method):',Int2)
print('Integration by simpson method:',simps(f(x),x))




##Gaussian Function Integration
f=lambda z: (1/(2*np.pi)**0.5)*np.exp((-z**2)/2)  #function to integrate
a, b= 0, 2*np.pi                         #x Limits
N= 10000                               #No. of random points projected
x=np.linspace(a,b,10000)                 

y_min, y_max= 0, np.max((f(x)))+1       #y Limits
A=(b-a)*(y_max-y_min)                   #Area of total random limit

X= np.random.uniform(a, b, N)           
Y= np.random.uniform(y_min, y_max, N)   
n=np.sum([abs(Y)<=abs(f(X))])           #Dots inside the function

plt.scatter(X, Y, c='r', s=.5, antialiased=False)
plt.plot(x, f(x), c='blue',label='f(x)')
plt.grid()
plt.xlabel(r'X$\longrightarrow$')
plt.ylabel(r'Y$\longrightarrow$')
plt.title('Gaussian Function Integration Monte Carlo Method')
plt.show()

Int=(b-a)*np.mean(f(X))
Int2=A*n/N

print('\n Gaussian Function Integration')
print('Integration by Monte Carlo Method(Functional):',Int)
print('Integration by Monte Carlo Method(Dot method):',Int2)
print('Integration by simpson method:',simps(f(x),x))



##Gamma Function Integration
f=lambda z: z**0.5*np.exp(-z)  #function to integrate
a, b= 0, 2*np.pi                         #x Limits
N= 10000                               #No. of random points projected
x=np.linspace(a,b,10000)                 

y_min, y_max= 0, np.max((f(x)))+1       #y Limits
A=(b-a)*(y_max-y_min)                   #Area of total random limit

X= np.random.uniform(a, b, N)           
Y= np.random.uniform(y_min, y_max, N)   
n=np.sum([abs(Y)<=abs(f(X))])           #Dots inside the function

plt.scatter(X, Y, c='r', s=.5, antialiased=False)
plt.plot(x, f(x), c='blue',label='f(x)')
plt.grid()
plt.xlabel(r'X$\longrightarrow$')
plt.ylabel(r'Y$\longrightarrow$')
plt.title('Gamma Function Integration Monte Carlo Method')
plt.show()

Int=(b-a)*np.mean(f(X))
Int2=A*n/N

print('\n Gamma Function Integration')
print('Integration by Monte Carlo Method(Functional):',Int)
print('Integration by Monte Carlo Method(Dot method):',Int2)
print('Integration by simpson method:',simps(f(x),x))



##Exponential Function Integration
f=lambda z: np.exp(2*z)  #function to integrate
a, b= 0, np.pi                         #x Limits
N= 1000000                             #No. of random points projected
x=np.linspace(a,b,100000)                 

y_min, y_max= 0, np.max((f(x)))+1       #y Limits
A=(b-a)*(y_max-y_min)                   #Area of total random limit

X= np.random.uniform(a, b, N)           
Y= np.random.uniform(y_min, y_max, N)   
n=np.sum([abs(Y)<=abs(f(X))])           #Dots inside the function

plt.scatter(X, Y, c='r', s=.5, antialiased=False)
plt.plot(x, f(x), c='blue',label='f(x)')
plt.grid()
plt.xlabel(r'X$\longrightarrow$')
plt.ylabel(r'Y$\longrightarrow$')
plt.title('Exponential Function Integration Monte Carlo Method')
plt.show()

Int=(b-a)*np.mean(f(X))
Int2=A*n/N

print('\n Exponential Function Integration')
print('Integration by Monte Carlo Method(Functional):',Int)
print('Integration by Monte Carlo Method(Dot method):',Int2)
print('Integration by simpson method:',simps(f(x),x))



f=lambda z: z/(np.exp(z)-1)  #function to integrate
a, b=0.00001, 2*np.pi                         #x Limits
N= 1000000                             #No. of random points projected
x=np.linspace(a,b,10000)                 

y_min, y_max= 0, np.max((f(x)))+1       #y Limits
A=(b-a)*(y_max-y_min)                   #Area of total random limit

X= np.random.uniform(a, b, N)           
Y= np.random.uniform(y_min, y_max, N)   
n= np.sum([abs(Y)<=abs(f(X))])           #Dots inside the function

plt.scatter(X, Y, c='r', s=.5, antialiased=False)
plt.plot(x, f(x), c='blue',label='f(x)')
plt.grid()
plt.xlabel(r'X$\longrightarrow$')
plt.ylabel(r'Y$\longrightarrow$')
plt.title('Monte Carlo Method')
plt.show()

Int=(b-a)*np.mean(f(X))
Int2=A*n/N

print('\n f(z) = z/(e^z-1) integration')
print('Integration by Monte Carlo Method(Functional):',Int)
print('Integration by Monte Carlo Method(Dot method):',Int2)
print('Integration by simpson method:',simps(f(x),x))



##Sinc Function Integration
f=lambda z: np.sin(z)/z  #function to integrate
a, b=0.00001, np.pi/2                         #x Limits
N= 10000                               #No. of random points projected
x=np.linspace(a,b,10000)                 

y_min, y_max= 0, np.max((f(x)))+1       #y Limits
A=(b-a)*(y_max-y_min)                   #Area of total random limit

X= np.random.uniform(a, b, N)           
Y= np.random.uniform(y_min, y_max, N)   
n=np.sum([abs(Y)<=abs(f(X))])           #Dots inside the function

plt.scatter(X, Y, c='r', s=.5, antialiased=False)
plt.plot(x, f(x), c='blue',label='f(x)')
plt.grid()
plt.xlabel(r'X$\longrightarrow$')
plt.ylabel(r'Y$\longrightarrow$')
plt.title('Sinc Function Integration Monte Carlo Method')
plt.show()

Int=(b-a)*np.mean(f(X))
Int2=A*n/N

print('\n Sinc Function Integration')
print('Integration by Monte Carlo Method(Functional):',Int)
print('Integration by Monte Carlo Method(Dot method):',Int2)
print('Integration by simpson method:',simps(f(x),x))

