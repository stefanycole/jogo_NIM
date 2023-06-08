def computador_escolhe_jogada(n, m):
    if n <= m:
         return n
    else:
         jogada = (n % (m + 1))
         if jogada > 0:
             return jogada 
         else:
             return m

def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada == 0:
         jogada = int(input("Quantas peças você vai tirar? "))
         if jogada < 1 or jogada > m or jogada > n:
             print("\nOops! Jogada inválida! Tente de novo.\n")
             jogada = 0
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    usuario_joga = False
    if n % (m + 1) == 0:
        print("\nVocê começa!\n")
        usuario_joga = True
    else:
        print("\nComputador começa!\n")
    
    while n > 0:
         if usuario_joga:
              jogada = usuario_escolhe_jogada(n, m)
              usuario_joga = False
              print("Voce tirou", jogada, "peça(s).")
              n = n - jogada
              if n == 0:
                 print("Fim do jogo! O usuario ganhou!")
                 return 1
              else:
                 print("Agora resta apenas", n, "peça(s) no tabuleiro.\n")
         else:
              jogada = computador_escolhe_jogada(n, m)
              usuario_joga = True
              print("O computador tirou", jogada, "peça(s).")
              n = n - jogada
              if n == 0:
                 print("Fim do jogo! O computador ganhou!")
                 return 0
              else:
                 print("Agora resta apenas", n, "peça(s) no tabuleiro.\n")

def campeonato():
    placar_usuario = 0
    placar_computador = 0
    rodada = 1

    while rodada <= 3:
        print("\n**** Rodada", rodada, "****\n")
        resultado = partida()
        if resultado == 1:
            placar_usuario = placar_usuario + 1
        else:
            placar_computador = placar_computador + 1
        rodada = rodada + 1
    print("**** Final do campeonato! ****\n")
    print("Placar: Voce", placar_usuario, "X", placar_computador, "Computador")

print("Bem-vindo ao jogo do NIM! Escolha: \n")
x = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
if x == 1:
    print("\nVoce escolheu uma partida isolada!\n")
    partida()
else:
    if x == 2:
        print("\nVoce escolheu um campeonato!")
        campeonato()
    else:
        print("Opção invalida!")