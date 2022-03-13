""" Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços. """

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for row in range(altura):
    for col in range(largura):
        if row == 0 or row == altura - 1:
            print("#", end="")
        else:
            if col == 0 or col == largura - 1:
                print("#", end="")
            else:
                print(" ", end="")
    print("")

