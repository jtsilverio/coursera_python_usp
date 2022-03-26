""" 
Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
"""

def remove_repetidos(numbers):
    numbers.sort()
    numbers_unique = []
    numbers_unique.append(numbers[0]) 

    for i in range(1, len(numbers)):
        if numbers_unique[len(numbers_unique)-1] != numbers[i]:
            numbers_unique.append(numbers[i])

    return numbers_unique