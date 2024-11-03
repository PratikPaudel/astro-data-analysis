import numpy as np
import matplotlib.pyplot as plt

# Basic function plotting examples
def plot_quadratic():
    x = np.linspace(-10, 10, 1000)
    a, b, c = 3, 1, 4
    y = a*x**2 + b*x + c

    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title("Quadratic Function")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.grid(True)
    plt.show()

def plot_cubic():
    x = np.arange(-11, 11, 1)
    a, b, c, d = 2, 3, 4, 9
    y = a*(x**3) + b*(x**2) + c*x + d

    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title("Cubic Function")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.grid(True)
    plt.show()

def plot_log():
    x = np.arange(1, 11, 0.001)
    y = np.log(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title("Natural Logarithm Function")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.grid(True)
    plt.show()

def plot_trigonometric():
    t = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(t)
    y = np.sin(t)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title("Parametric Circle")
    plt.xlabel("cos(t)")
    plt.ylabel("sin(t)")
    plt.grid(True)
    plt.show()

# Run all plots
if __name__ == "__main__":
    plot_quadratic()
    plot_cubic()
    plot_log()
    plot_trigonometric()