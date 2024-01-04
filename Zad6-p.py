import numpy as np
import matplotlib.pyplot as plt

# Funkcja ReLU
def relu(x):
    return np.maximum(0, x)

# Gradient funkcji ReLU
def relu_gradient(x):
    return np.where(x > 0, 1, 0)

# Zakres danych x
x = np.linspace(-7, 7, 200)

# Obliczamy wartości funkcji ReLU i jej gradientu
relu_values = relu(x)
relu_gradient_values = relu_gradient(x)

# Tworzymy wykres
plt.figure(figsize=(8, 6))
plt.plot(x, relu_values, label='ReLU')
plt.plot(x, relu_gradient_values, label='Gradient ReLU')
plt.legend()
plt.xlabel('x')
plt.ylabel('Wartosc')
plt.title('Funkcja ReLU i jej Gradient')
plt.grid(True)
plt.show()
