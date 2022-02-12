"""
Escreva um programa que receba um número inteiro na entrada, 
calcule e imprima a soma dos dígitos deste número na saída
"""

n = int(input("Digite um número inteiro: "))

soma = 0
while n > 10:
    ultimo_digito = n % 10
    soma = ultimo_digito + soma
    n = n // 10
soma = soma + n

print(soma)
