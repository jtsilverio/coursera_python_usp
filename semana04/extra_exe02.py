""" Escreva um programa que receba um número inteiro na entrada
e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele.
Caso exista, imprima "sim"; se não existir, imprima "não".
 """

n = int(input("Digite um número inteiro: "))

while n > 10:
    ultimo_digito = 