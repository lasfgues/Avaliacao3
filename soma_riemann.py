import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol('x')

def soma_riemann(expression, a, b, n):
  try:
    expr = sp.sympify(expression, locals={"e": sp.E, "pi": sp.pi})
    f_lambd = sp.lambdify(x, expr, modules=["numpy"])

    a, b, n = int(a), int(b), int(n)

    dx = (b - a) / n

    x_vals = np.linspace(a, b - dx, n)
    y_vals = f_lambd(x_vals)

    x_curve = np.linspace(a, b, 400)
    y_curve = f_lambd(x_curve)

    plt.figure(figsize=(10, 6))
    plt.plot(x_curve, y_curve, label=f"f(x) = {expression}")
    plt.bar(x_vals, y_vals, width=dx, align='edge', alpha = 0.5, edgecolor='black', label=f'Retângulos')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Soma de Riemann para f(x) = {expression}")
    plt.grid(True)
    plt.legend()
    plt.show()

    soma_aprox = np.sum(y_vals * dx)
    return float(soma_aprox)

  except Exception as e:
      return f"Erro: {e}"

func, a, b, n = input('Função: '), input('Intervalo a: '), input('Intervalo b: '), input('Divisões: ')

soma_riemann(func, a, b, n)
