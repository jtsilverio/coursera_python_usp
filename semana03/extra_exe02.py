""" Exercício 2 - Desafio da videoaula

Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.

O programa deve receber os parâmetros a, b, e c da equação ax2+bx+c, respectivamente, 
e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:

    esta equação não possui raízes reais

Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:
    a raiz desta equação é X
ou
    a raiz dupla desta equação é X
    onde X é o valor da raiz dupla

Quando houver duas raízes reais imprima:
    as raízes da equação são X e Y
    onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente. Exemplos:
    as raízes da equação são 1.0 e 2.0
    as raízes da equação são -2.0 e 0.0 """

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

delta = b**2 - 4 * a * c
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    if delta == 0:
        x = -b / (2 * a)
        print("a raiz desta equação é", x)
    else:
        x = []
        x.append((-b + delta**(1 / 2)) / (2 * a))
        x.append((-b - delta**(1 / 2)) / (2 * a))
        x = sorted(x)
        print("as raízes da equação são", x[0], "e", x[1])
