"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Random Walk in 1D
Author       : Chitrak Roychowdhury
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

N,T=3000,50          # N= Ensemble number & T= time step
t=range(1,T+1)
walks= np.random.choice((-1,1),size=(N,T))

#################################################################
# Trajectory of the walker

plt.plot(np.cumsum(walks),'--',color='red')
plt.title("Trajectory")
plt.grid(True)
plt.savefig("randomwalk_1D(0).pdf")
plt.show()

#################################################################
# (a) Calculation of mean and mean square displacement:

positions=np.cumsum(walks,axis=1)
mean_pos=np.mean(positions,axis=0)
print('The mean of 50 random walks is: ', mean_pos[-1])

positions=np.cumsum(walks,axis=1)
pos_sq = positions**2                     #square of positions
mean_pos_sq= np.mean(pos_sq,axis=0)       #mean of square of positions
print('The mean square of 50 random walks is: ' , mean_pos_sq[-1])


#################################################################
# (b) Plotting of mean and mean square displacement vs no of steps

positions=np.cumsum(walks,axis=1)
mean_pos=np.mean(positions,axis=0)
pos_sq=positions**2
mean_pos_sq= np.mean(pos_sq,axis=0)


#plot fitting for mean vs no of steps

coeffs_mean=poly.polyfit(t,mean_pos,1)
mean_coeffs= coeffs_mean[1]*t+coeffs_mean[0]
plt.title('Mean of 50 random walks vs no of steps')
plt.xlabel('No of steps $\longrightarrow $')
plt.ylabel('Mean $\longrightarrow $')
plt.ylim(-5,5)
plt.plot(t,mean_pos,'o', label='mean displacement(sampled)')
plt.plot(t,mean_coeffs,'-', label='mean displacement(fitted)')
plt.legend(loc='best')
plt.grid("True")
plt.savefig("randomwalk_1D(1).pdf")
plt.show()


#plot fitting for mean square vs no of steps

coeffs_mean_sq=poly.polyfit(t,mean_pos_sq,1)
mean_coeffs_sq= coeffs_mean_sq[1]*t+coeffs_mean_sq[0]
plt.title('Mean square of 50 random walks vs no of steps')
plt.xlabel('No of steps $\longrightarrow $')
plt.ylabel('Mean square $\longrightarrow $')
plt.plot(t,mean_pos_sq,'o', label='mean square displacement(sampled)')
plt.plot(t,mean_coeffs_sq,'-', label='mean square displacement(fitted)')
plt.legend(loc='best')
plt.grid("True")
plt.savefig("randomwalk_1D(2).pdf")
plt.show()

#################################################################
# (c) Slope of mean and mean square curve :

print('slope of mean displacement vs step curve is : ', mean_coeffs[1])
print('slope of mean square displacement vs step curve is : ', mean_coeffs_sq[1])


#################################################################
# (d) Probability of taking n steps to the right out of N steps :

Ts=int(input('Enter total number of steps taken:'))
n=int(input('Enter no of steps taken to the right:'))
def ProbRight(n,Ts):
    ran_walk=walks[:,:Ts]
    c=0
    for i in range(n):
        count=np.unique(ran_walk[i],return_counts=True)[1][1]
        if count==n:
            c+=1
    P=c*1./N
    return P
prob=np.vectorize(ProbRight)
pdf=prob(t,T)

print('The probability of',n,'right steps out of',Ts,'steps is :',prob(n,T))

###########################################################################

# (e) Probability distribution function:

plt.grid()
plt.bar(t,pdf,color='red')
plt.title(' Probability distribution function ')
plt.xlabel(r'Steps$\longrightarrow$')
plt.ylabel(r'P.D.F$\longrightarrow$')
plt.savefig("randomwalk_1D(3).pdf")
plt.show()
