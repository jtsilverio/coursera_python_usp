""" Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída. """

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for row in range(altura):
    for col in range(largura):
        print("#", end="")
    print("")

