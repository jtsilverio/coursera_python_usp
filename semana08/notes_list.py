# slicing
numeros = list(range(20))
numeros[0:3] # A ultima posição não é inclusa
numeros[:3] # maneira abreviada. Vai do elemento 0 ao elemento 2
numeros[3:] # vai até o final

# clonando listas
# ao atribuir listas ele nao copia a lista 
# ele copia apenas a referencia da lista
numeros_2 = numeros
numeros[0] = 1
numeros
numeros_2

# pra isso usar o método .copy
numeros = list(range(20))
numeros_2 = numeros.copy()
numeros[0] = 1
numeros
numeros_2


# ou slicing
numeros = list(range(20))
numeros_2 = numeros[:]
numeros[0] = 1
numeros
numeros_2

# Pertencimento
# operador 'in'

2 in numeros
50 in numeros

# concatenacao
# 'soma' de lista
numeros = list(range(20))
numeros_2 = numeros[:]
numeros[0] = 1
numeros + numeros_2

# nao funciona para copia de lista
x = numeros + numeros_2
numeros = (numeros + numeros_2)
numeros

# append
# altera uma lista existente
numeros.append("a")
numeros

# remocao
# comando 'del'
numeros = list(range(20))
del(numeros[2])
numeros