"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Einstein model
Author       : Chitrak Roychowdhury
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#constants
h = 6.62606896E-34 ; hbar=(h/(2*np.pi)) ; kb = 1.3806504E-23
Na = 6.02214076E23 #Avogadro's Number
Mw = 63.546 #Molecular wt of Cu(gm/mole)
rho = 8960.0 #Density of Cu(kg/m**3)
nv = 1000*Na*rho/Mw
Y = 0.76E11 #Young's Modulus of Cu
vs = np.sqrt(Y/rho)  #velocity of sound in Cu
ome = (vs/2)*(nv)**(1./3)*2.0*np.pi #density of states
Te = (hbar*ome)/kb #Einstein's temp
T=np.linspace(1,Te,50)
C=np.zeros(len(T)) ; clt=np.zeros(len(T)) ; cht=np.zeros(len(T))

for i in range(len(T)):
    xE=Te/T[i]
    C[i]=(3*Na*kb)*xE**2*((np.exp(xE))/(np.exp(xE)-1)**2)
    clt[i]=(3*Na*kb)*xE**2*(np.exp(-xE))
    cht[i]=3*Na*kb

plt.plot(T,clt, ls='-.',label='Cv at low temp ')
plt.plot(T,cht, ls='-.',label='Cv at high temp ')
plt.plot(T,C)
plt.xlabel('Temparature $\longrightarrow$')
plt.ylabel('$C_v $ $\longrightarrow$')
plt.legend()
plt.grid()
plt.title("Einstein Model of specific heat")
plt.savefig("Einstein.pdf")
plt.show()

