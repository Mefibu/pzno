import sympy as sp

# Определяем переменную a
a = sp.Symbol('a')

# Записываем выражение
expression = sp.root(
    (a**3 - 3*a**2 + 3*a - 1) * ((a**2 - 4) * (a - 2) - (4*a**2 - 4*a - 5) / (4*a + 2)),
    4
)

# Упрощаем выражение
simplified_expr = sp.simplify(expression)
print(f'Упрощенное выражение: {simplified_expr}')

# Подставляем значение a = 4 и вычисляем результат
value_at_4 = simplified_expr.subs(a, 4)
print(f'Значение выражения при a = 4: {value_at_4}')
