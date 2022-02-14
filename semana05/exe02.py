""" Escreva a função maior_primo que recebe um número inteiro maior ou igual a  como parâmetro e devolve o maior número primo menor ou igual ao número passado à função """


def maior_primo(n):
    if n > 2:
        while n > 2:
            if isPrime(n):
                return n
            n -= 1
    else:
        return "numero deve ser maior que 2"

def isPrime(n):
    if n % 2 == 0:
        return False
    else:
        i = 3
        while i < n:
            if n % i == 0:
                return False
            i = i + 2
        return True
