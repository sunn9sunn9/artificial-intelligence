import numpy as np
import random
import matplotlib.pyplot as plt
sluchmassiv = [random.random() for _ in range(200)]
srednee = np.mean(sluchmassiv)
mediannoe = np.median(sluchmassiv)
print("Случайный массив:", sluchmassiv)
print("Среднее значение = ", srednee)
print("Медианное значение = ", mediannoe)
plt.scatter(range(len(sluchmassiv)), sluchmassiv, marker='o', color='blue', label='Точки')
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.title('Точечная диаграмма рассеяния')
plt.legend()
plt.show()
