import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

# Valores de x (de 0 a 10 com passos pequenos)
x = np.linspace(0, 10, 100)

# Função exponencial y = 2 * 1.5^x
y = 2 * (1.5 ** x)

# Plot
plt.plot(x, y, label='y = 2 * 1.5^x', color='red')
plt.title("Gráfico da Função Exponencial")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.show()
 