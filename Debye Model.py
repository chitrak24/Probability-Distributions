#Debye model of specific heat(Teat case copper)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

h=6.62606896E-34
hbar=(h/(2*np.pi))
kb=1.3806504E-23
Na=6.02214076E23        #avogrado no
Mw=63.546
rho=8960.0
V_Transverse=2325.0     #in m/s
V_Longitudinial=4760.0  #in m/s

vs=3**(1/3)*(2.0/V_Transverse**3 + 1/(V_Longitudinial)**3)**(-1/3)
nv=1000*Na*rho/Mw              #N/V=rho Na /Mw
omD=vs*(6*np.pi**2*nv)**(1/3)  # Debye cutoff frequency
thD=(hbar*omD)/kb              #Debye temparature
T=np.arange(0.,thD,5)
T[0]=1
c=np.zeros(len(T));clt=np.zeros(len(T));cht=np.zeros(len(T));

for i in range(len(T)):
      xD=thD/(T[i])
      I=quad(lambda x: (x**4*np.exp(x))/((np.exp(x)-1)**2),0,xD)[0]
      c[i]=9*Na*kb*((T[i]/thD)**3)*I
      clt[i]=((12.0/5)*(np.pi**4)*Na*kb*(T[i]**3))/thD**3
      cht[i]=3*Na*kb

plt.title('Cv vs Debye Temp graph')
plt.xlabel('Temparature $\longrightarrow$')
plt.ylabel('$C_v $ $\longrightarrow$')
plt.grid()
plt.ylim(0,40)
plt.plot(T,c,label='Cv ')
plt.plot(T,clt,ls='-.',label='Cv at low temp ')
plt.plot(T,cht,ls='--',label='Cv at high temp')
plt.legend()
plt.savefig("debye.pdf")
plt.show()
