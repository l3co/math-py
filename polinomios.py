"""
Operações com polinomios acontecem com a função numpy
Primeiramente precisamos importar a numpy para utilizar a operação
"""

from numpy import polyadd, polysub, polymul, polydiv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('\n' * 100)

    # Adição de polinômios
    coeficientes_pol1 = [3,2,-1] # Define polinomios 3x**2 + 2x - 1
    coeficientes_pol2 = [4,-1,3] # Define polinomios 4x**2 - x + 3

    resultado_add = polyadd(coeficientes_pol1, coeficientes_pol2)

    print("Print resultado da soma entre polinomios")
    print("(3x**2 + 2x - 1)", " + ", "(4x**2 - x + 3)")
    print(f"{resultado_add=}")


    resultado_sub = polysub(coeficientes_pol1, coeficientes_pol2)

    print("Print resultado da subtração entre polinomios")
    print("(3x**2 + 2x - 1)", " - ", "(4x**2 - x + 3)")
    print(f"{resultado_sub=}")

    resultado_mult = polymul(coeficientes_pol1, coeficientes_pol2)

    print("Print resultado da multiplicação entre polinomios")
    print("(3x**2 + 2x - 1)", " * ", "(4x**2 - 1x + 3)")
    print(f"{resultado_mult=}")