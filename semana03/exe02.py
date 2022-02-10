""" Exercícios 2 - FizzBuzz parcial, parte 1

Receba um número inteiro na entrada e imprima 
    Fizz
se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada. """

number = int(input("Digite um número: "))

if number % 3 == 0:
    print("Fizz")
else:
    print(number)

