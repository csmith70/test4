from scipy.optimize import fsolve
import numpy as np
B =  6130.
a = 3.41E9
w = .0033
p = 80.
T = 268.
e=.622
f = lambda x: (B/(np.log(((a*e)/(w*p))*((T/x)**(1/.286))))) - x
root = fsolve(f, [260.,290.])
print(root)
