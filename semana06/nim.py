import time

def main():
    print("Bem-vindo ao jogo do NIM!")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    escolha = int(input("Escolha: "))
    while not(escolha in range(1,3)):
        escolha = int(input("Escolha uma opção valida."))
    
    if escolha == 1:
        partida()
    else:
        campeonato()

def campeonato():
    placar = [0, 0]
    for i in range(1,4):
        print("\n**** Rodada", i, "****\n")
        if partida() == "usuario":
            placar[0] += 1
        else:
            placar[1] += 1
    
    print("\n**** Final do campeonato! ****")
    print("Placar: Você", placar[0], "X", placar[1], "Computador")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m+1) == 0:
        print("Você começa!")
        ultima_jogada = "usuario"
        r = usuario_escolhe_jogada(n, m)
        n = n - r
    else:
        print("Computador começa!")
        ultima_jogada = "computador"
        r = computador_escolhe_jogada(n, m)
        n = n - r

    while n != 0:
        if ultima_jogada == "usuario":
            r = computador_escolhe_jogada(n, m)
            n = n - r
            ultima_jogada = "computador"

        else:
            r = usuario_escolhe_jogada(n, m)
            n = n - r
            ultima_jogada = "usuario"
        
    print("Fim do jogo! O", ultima_jogada, "ganhou!")
    return ultima_jogada

def computador_escolhe_jogada(n, m):
    if n > m:
        for i in range(1, m+1):
            if (n - i) % (m + 1) == 0:
                
                if i == 1:
                    print("Computator tirou uma peça.")
                else:
                    print("Computator retirou", i, "peças.")
                
                if n - i == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora restam", n - i, "peças no tabuleiro.")

                return i
    else:
        print("Computator tirou", n, "peças.")
        return n

def usuario_escolhe_jogada(n, m):
    r = int(input("Quantas peças você vai tirar?: "))
    if r > m or r <= 0:
        while r > m or r <= 0:
            print("Oops! Jogada inválida! Tente de novo.")
            r = int(input("Quantas peças você vai tirar?: "))
    elif n <= m and r > n:
        print("Oops! Jogada inválida! Tente de novo.")
        r = int(input("Quantas peças você vai tirar?: "))  
    
    if (r == 1):
        print("Você tirou uma peça")
    else:
        print("Você tirou", r,"peças.")

    if n - r == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
    else:
        print("Agora restam ", n - r, "peças no tabuleiro.")
    
    return r

main()