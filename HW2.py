import numpy as np
import scipy 
from scipy.special import gamma
import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad
z = gamma(1.5)
N = 5600
d = 4E-5
def integrand(D,N,z,d):
    return ((np.pi)/6)*(D**3)*(-.193+(4960*D)-(9.04E5*(D**2))+(5.66E7*(D**3)))*(N*((D**0.5)/(z*(d**1.5))*np.exp(-D/d)))

I = quad(integrand,0,np.Inf,args=(N,z,d))
print(I)


