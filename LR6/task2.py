from scipy import integrate
import numpy as np

f = lambda y, x: np.exp(-x**2 - y**2)
res, _ = integrate.dblquad(f, 0, 1, lambda x: 0, lambda x: 1)
print("Double integral result:", res)