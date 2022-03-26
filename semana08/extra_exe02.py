"""
Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.
"""


def main():
    lista = []
    n = int(input("Digite um número: "))

    while n != 0:
        lista.append(n)
        n = int(input("Digite um número: "))

    lista = reverse_list(lista)
    print(*lista, sep = "\n")


def reverse_list(lista):
    list_rev = []
    for i in range(len(lista)):
        list_rev.append(lista[(i+1)*-1])
        # could also do:
        # lista.reverse()
        # lista_rev = list[::-1]

    return list_rev


main()