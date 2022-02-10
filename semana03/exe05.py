""" Exercício 5 - Verificando ordenação

Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima 

não está em ordem crescente """

numbers = []
for i in range(3):
    numbers.append(int(input("Digite um Número: ")))

if(numbers == sorted(numbers)): # vai ser um pouco lento se a lista for grande
    print("crescente")
else:
    print("não está em ordem crescente")