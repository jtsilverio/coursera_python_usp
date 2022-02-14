""" Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. 
Se o número for primo, imprima "primo".
Caso contrário, imprima "não primo". """

n = int(input("Digite um número inteiro: "))

primo = True
if n <= 1:
    primo = False
elif n == 2:
    primo = False
elif n > 2 and n % 2 == 0: # Checa se é par
    primo = False
elif primo:
    i = 3
    while i < n: # um pouco ineficiente
        if n % i == 0:
            primo = False
        i = i + 2

if primo:
    print("primo")
else:
    print("não primo")