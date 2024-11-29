import sympy as sp

# Определяем переменные и функцию
x = sp.Symbol('x')
y = sp.Function('y')

# Задаем дифференциальное уравнение
deq = y(x).diff(x, x) - 3 * y(x).diff(x) + y(x) - sp.cos(x)

# Решаем дифференциальное уравнение
solution = sp.dsolve(deq)

# Выводим общее решение дифференциального уравнения
print('Общее решение дифференциального уравнения:')
sp.pprint(solution)
