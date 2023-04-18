import numpy as np
import matplotlib.pyplot as plt

# Isolando y em cada equação
# 2x + 3y = 6
# 3y = -2x + 6
# y = (-2/3)x + 2

# -x + 2y = 2
# 2y = x + 2
# y = (1/2)x + 1

# Coeficiente angular de cada equação
coef_angular1 = -2/3
coef_angular2 = 1/2

# Verificando se as linhas são paralelas
if coef_angular1 == coef_angular2:
    print("As linhas são paralelas.")
else:
    # Calculando o ponto de interseção das linhas
    # 2x + 3y = 6
    # -x + 2y = 2
    A = np.array([[2, 3], [-1, 2]])
    B = np.array([6, 2])
    x, y = np.linalg.solve(A, B)
    print("O ponto de interseção das linhas é:", x, y)


    # Valores de x em um intervalo
    x = np.linspace(-5, 5, 100)

    # Valores correspondentes de y para cada equação
    y1 = coef_angular1 * x + 2
    y2 = coef_angular2 * x + 1

    # Plotando as duas linhas no mesmo gráfico
    plt.plot(x, y1, label='2x+3y=6')
    plt.plot(x, y2, label='-x+2y=2')


    # Configurações do gráfico
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()
