import sympy as sp

# Найти все решения системы уравнений
x, y, z = sp.symbols('x y z')
system = [
    x*y - z**2 - 1,
    y*z - x**2 - 2,
    z*x - y**2 - 3
]
solutions_system = sp.solve(system, (x, y, z))
print(f'Решения системы уравнений: {solutions_system}')
