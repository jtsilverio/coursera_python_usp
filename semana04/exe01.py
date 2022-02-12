# Escreva um programa que receba um número natural n
# na entrada e imprima n! n! n! (fatorial) na saída.

n = int(input("Digite o valor de n: "))

f = 1
while n >= 1:
    f = f * n
    n = n - 1

print(f)
