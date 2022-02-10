""" Exercício 1 - Par ou ímpar?

Receba um número inteiro na entrada e imprima
    par 
quando o número for par ou
    ímpar
quando o número for ímpar. """

number = int(input("Digite um número: "))

if number % 2 == 0:
    print("par")
else:
    print("ímpar")
