import numpy as np
import matplotlib.pyplot as plt
from random import choice
import numpy.polynomial.polynomial as poly

#####################################################################################
# (a) Calculation of mean square displacement and end to end displacement:

def rand_walks(steps):
    x,y = 0,0
    dis_sq = []
    for i in range (steps):
        dx,dy = choice([(1,0),(-1,0),(0,1),(0,-1)])
        x,y = x+dx,y+dy
        dis_sq.append(x**2+y**2)
    return dis_sq

steps = 50        #no of steps
samples = 10000   #n of random walks
r = range(1,steps+1)

walks = np.array([rand_walks(steps) for i in range(samples)])
msq_disp = np.mean(walks,axis=0)                                 #mean square displacement
print("Mean square displacement after 50 random steps",msq_disp[-1])


#####################################################################################
# (b) Plot of mean sq disp vs no of steps :

coeffs=poly.polyfit(r,msq_disp,1)
msq_fit=coeffs[1]*r+coeffs[0]

plt.title('Mean Squared displacement vs Step')
plt.plot(r,msq_disp,'o',label='mean square displacement(sampled)')
plt.plot(r,msq_fit,'-',label='mean square displacement(fitted)')
plt.xlabel(r'Steps$\longrightarrow$')
plt.ylabel(r'Mean Squared displacement$\longrightarrow$')
plt.legend(loc='best')
plt.grid(True)
plt.savefig("rd_walk_2D.pdf")
plt.show()

#Slope 
print('slope of mean square displacement vs step curve:',coeffs[1])
