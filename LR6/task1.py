import numpy as np
from scipy import integrate

# Вычисление интеграла тремя способами
f = lambda x: np.exp(-x**2)

# quad
quad_res, _ = integrate.quad(f, 0, 1)

# fixed_quad
fixed_quad_res, _ = integrate.fixed_quad(f, 0, 1, n=5)

# quadrature
quadrature_res, _ = integrate.quadrature(f, 0, 1)

print("quad:", quad_res)
print("fixed_quad:", fixed_quad_res)
print("quadrature:", quadrature_res)