import math
import matplotlib.pyplot as plt
from scipy.integrate import trapz
import numpy as np
def y(x):
    return ((math.cos((x * 2.71828182846) ** (math.cos(x) + math.log(x + 1)))) ** 0.5) ** 2
x = np.arange(0, 11, 1)
y_values = [y(xi) for xi in x]
plt.fill_between(x, y_values, alpha=0.3)
plt.plot(x, y_values, label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y(x)')
plt.legend()
plt.grid(True)
plt.show()
area = trapz(y_values, x)
print(f"Площадь под графиком: {area}")
