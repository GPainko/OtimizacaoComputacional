import numpy as np
import matplotlib.pyplot as plt

# Define as restrições
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
ya = -x + 6
yb = 6 + 0*x
yc = x + 4
yd = 2*x + 2
ye = x - 3
xf = 5 + 0*y

# Define as regiões viáveis
y1 = np.maximum(0, ya)
y2 = np.maximum(0, yb)
y3 = np.maximum(0, yc)
y4 = np.maximum(0, yd)
y5 = np.maximum(0, ye)
y6 = np.maximum(xf, 0)

# Encontra os pontos de interseção das restrições
A = np.array([
    [1, 1],
    [-2, 1]
])
b = np.array([6,2])
x_int1, y_int1 = np.linalg.solve(A, b)

A = np.array([
    [1, 1],
    [-1, 1]
])
b = np.array([6, -3])
x_int2, y_int2 = np.linalg.solve(A, b)

# Cria o gráfico
fig, ax = plt.subplots()
ax.plot(x, ya, label='- x + y - 6')
ax.plot(x, yb, label='y <= 6')
ax.plot(x, yc, label='- x + y - 4 <= 0')
ax.plot(x, yd, label='-2x + y - 2 >= 0')
ax.plot(x, ye, label='x - y - 3 <= 0')
ax.plot(xf, y, label='x <= 5')

ax.fill_between(x, y1, color='orange', alpha=0.2)
ax.fill_between(x, y2, color='blue', alpha=0.2)
ax.fill_between(x, y3, color='green', alpha=0.2)
ax.fill_between(x, y4, color='red', alpha=0.2)
ax.fill_between(x, y5, color='purple', alpha=0.2)
ax.fill_betweenx(y, y6, color='pink', alpha=0.2)

ax.plot(x_int1, y_int1, 'ro', markersize=8)
ax.plot(x_int2, y_int2, 'ro', markersize=8)
ax.plot(3, 0, 'ro', markersize=8)
ax.plot(0, 2, 'ro', markersize=8)

ax.set_xlim((0, 7))
ax.set_ylim((0, 7))
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.legend(loc='upper right')
plt.show()
