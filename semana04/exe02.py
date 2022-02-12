# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.
# Para a saída, siga o formato do exemplo abaixo.

n = int(input("Digite o valor de n: "))

i = 1
while n != 0:
    if i % 2 != 0:
        print(i)
        n -= 1
    i += 1
