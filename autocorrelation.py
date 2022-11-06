"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : AUTOCORRELATION
Author       : Chitrak Roychowdhury
"""

#using formula

import numpy as np
import matplotlib.pyplot as plt

n = 1000
x = np.random.uniform(0,1,n)

x_avg = np.mean(x) #Average of random numbers

coeff = lambda k: np.mean([( x[i] - x_avg )*( x[i+k] - x_avg )for i in range (n-k)])
r = lambda k: coeff(k)/coeff(0)
corr = [r(k) for k in range(100)]

print("Correlation Coefficients: ",corr)
plt.plot(corr,'--', color="magenta", label=r'ACF = $\frac{1}{n\sigma}\sum_{i=k+1}^{n}(x_i-\bar{x})(x_{i-k}-\bar{x})}$')
plt.legend(loc='best')
plt.title("Autocorrelation")
plt.ylabel("Correlation coefficients")
plt.xlabel("Lags")
plt.grid(True)
plt.savefig("autocorrelation(1).pdf")
plt.show()


#Using numpy.corrcoef

def autocorr(x,lags):  
    corr = [1. if l==0 else np.corrcoef(x[l:],x[:-l])[0][1] for l in lags]
    return np.array(corr)


# Main
y = np.random.randint(0,50,1000)
y = np.array(y).astype('float')
lags = np.arange(100); 

# Calculate ACF using different methods
acf = autocorr(y,lags)
print(acf)

# Plot
plt.figure()
plt.plot(lags, acf, '-o', lw='2', color="red", label=r'ACF = $\frac{1}{n\sigma}\sum_{i=k+1}^{n}(x_i-\bar{x})(x_{i-k}-\bar{x})}$')
plt.legend(loc='best')
plt.xlabel('Lag')
plt.ylabel('Correlation Coefficient')
plt.title('ACF of a Randomly distributed Time Series')
plt.xlim([-1.0, max(lags)+1])
plt.ylim([min(acf)-0.1, 1.1])
plt.grid()
plt.savefig("autocorrelation(2).pdf")
plt.show()
