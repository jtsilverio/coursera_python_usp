import re
import statistics

def main():
    ass_cp = le_assinatura() # threshold para grau de similaridade
    textos = le_textos()
    avalia_textos(textos, ass_cp)

    print(assinatura)

def wal(texto):
    '''Calcula o tamanho médio das palavras de uma lista de palavras'''
    palavras = separa_palavras()

    return


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("\nBem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto:

    - wal = Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    - ttr = Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    - hlr = Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
    - sal = Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    - sac = Complexidade de sentença: Média simples do número de frases por sentença.
    - pal = Tamanho médio de frase: Média simples do número de caracteres por frase.'''

    sentencas = separa_sentencas(texto)
    
    frases = []
    for s in sentencas:
        frases.extend(separa_frases(s))

    palavras = []
    for f in frases:
        palavras.extend(separa_palavras(f))

    wal = sum([len(p) for p in palavras])/len(palavras)
    ttr = n_palavras_diferentes(palavras)/len(palavras)
    hlr = n_palavras_unicas(palavras)/len(palavras)
    sal = sum([len(s) for s in sentencas])/len(sentencas)
    sac = len(frases)/len(sentencas)
    pal = sum([len(f) for f in frases])/len(frases)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    for texto in textos:
        ass_texto = calcula_assinatura(texto)
    
    

    
    return

main()

