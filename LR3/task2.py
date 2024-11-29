import numpy as np
import matplotlib.pyplot as plt

# Интервал для угла φ
phi = np.linspace(0, 2 * np.pi, 1000)

# Функция ρ = 1 - sin(φ)
rho = 1 - np.sin(phi)

# Построение графика в полярной системе координат
plt.figure(figsize=(6, 6))
plt.polar(phi, rho, color='orange', marker='^', linewidth=3)

# Заголовок графика
plt.title(r'График функции $\rho = 1 - \sin(\varphi)$ в полярной системе координат')

# Показать график
plt.show()
