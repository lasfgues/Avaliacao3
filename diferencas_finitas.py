import numpy as np
import sympy as sp

x = sp.Symbol('x')

expr_str = input("Função f(x): ")
x0 = float(input("Ponto x0: "))
h = float(input("Passo h: "))

expression = sp.sympify(expr_str, locals={"e": sp.E, "pi": sp.pi})
f_lambd = sp.lambdify(x, expression, modules=["numpy"])

f_xph = f_lambd(x0 + h)
f_xmh = f_lambd(x0 - h)

deriv_progr = (f_xph- f_lambd(x0)) / h
deriv_regr = (f_lambd(x0) - f_xmh) / h
deriv_central = (f_xph - f_xmh) / (2 * h)


f_prime = sp.diff(expression, x)
f_prime_lambd = sp.lambdify(x, f_prime, modules=["numpy"])
deriv_exata = f_prime_lambd(x0)

print(f"\nf(x) = {expression}")
print(f"Aproximação progressiva: f'(x) ≈ {deriv_progr:.6f}")
print(f"Aproximação regressiva: f'(x) ≈ {deriv_regr:.6f}")
print(f"Aproximação central: f'(x) ≈ {deriv_central:.6f}")
print(f"Derivada exata: f'(x)  = {deriv_exata:.6f}")
