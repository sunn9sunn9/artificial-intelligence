x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
srez = x[::2][::-1]
x[::2] = srez
print(x) 