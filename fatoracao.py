from sympy.abc import x
from sympy import factor

if __name__ == '__main__':
    print('\n' * 100)

    resultado=factor(x**2+3*x)
    print("Resultado da fatoração do polinômio x**2 + 3*x")
    print(resultado)

    resultado = factor(x ** 3 - 3 * x ** 2 - 10 * x)
    print('Resultado da fatoração do polinômio x**3 - 3*x**2 - 10*x')
    print(resultado)