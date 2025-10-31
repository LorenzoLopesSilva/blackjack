import random
import sys
import time
import os

def espera(tempo = 1):
    time.sleep(tempo)

def sair():
    sys.exit()

def apagar():
    os.system('cls')

def escolher_carta():

    cartas = [
    ("2 de Copas", 2),
    ("2 de Ouros", 2),
    ("2 de Espadas", 2),
    ("2 de Paus", 2),
    
    ("3 de Copas", 3),
    ("3 de Ouros", 3),
    ("3 de Espadas", 3),
    ("3 de Paus", 3),

    ("4 de Copas", 4),
    ("4 de Ouros", 4),
    ("4 de Espadas", 4),
    ("4 de Paus", 4),

    ("5 de Copas", 5),
    ("5 de Ouros", 5),
    ("5 de Espadas", 5),
    ("5 de Paus", 5),

    ("6 de Copas", 6),
    ("6 de Ouros", 6),
    ("6 de Espadas", 6),
    ("6 de Paus", 6),

    ("7 de Copas", 7),
    ("7 de Ouros", 7),
    ("7 de Espadas", 7),
    ("7 de Paus", 7),

    ("8 de Copas", 8),
    ("8 de Ouros", 8),
    ("8 de Espadas", 8),
    ("8 de Paus", 8),

    ("9 de Copas", 9),
    ("9 de Ouros", 9),
    ("9 de Espadas", 9),
    ("9 de Paus", 9),

    ("A de Copas", 10),
    ("A de Ouros", 10),
    ("A de Espadas", 10),
    ("A de Paus", 10),

    ("K de Copas", 10),
    ("K de Ouros", 10),
    ("K de Espadas", 10),
    ("K de Paus", 10),

    ("Q de Copas", 10),
    ("Q de Ouros", 10),
    ("Q de Espadas", 10),
    ("Q de Paus", 10),

    ("J de Copas", 10),
    ("J de Ouros", 10),
    ("J de Espadas", 10),
    ("J de Paus", 10),
 
]

    carta = random.choice(cartas)
    carta_nome = carta[0]
    valor_carta = carta[1]
    cartas.pop(cartas.index(carta))
    print(carta_nome)
    time.sleep(1)
    return valor_carta

def iniciar_menu():
    escolha_iniciar = int(input("Digite sua escolha: " \
    "\n 1- Iniciar Singleplayer " \
    "\n 2- Iniciar Multiplayer"
    "\n 3- Sair" \
    "\n"))

    if escolha_iniciar == 1:
        iniciar_jogo()
    elif escolha_iniciar == 2:
        apagar()
        iniciar_multiplayer()
    elif escolha_iniciar == 3:
        pass
    else:
        print("Escolha invalida")
        iniciar_menu()
    
def iniciar_jogo(vidas = 3):

    vidas = vidas


    print(f"Você tem {vidas} vidas.")

    cartas_usuario = escolha_menu()

    processo_vidas(cartas_usuario, vidas)

def processo_vidas(cartas_usuario, vidas):
    if cartas_usuario == None:
        vidas -= 1
        continuar(vidas)
    else: 
        print(f"Total do usuario: {cartas_usuario}")
        cartas_dealer = escolha_dealer(cartas_usuario)
        if cartas_dealer == None:
            continuar(vidas)
        elif cartas_usuario < cartas_dealer:
            vidas -= 1
            continuar(vidas)

def escolha_menu():

    print("Cartas do Usuario: ")
    carta_1 = escolher_carta()
    
    carta_2 = escolher_carta()
    cartas_usuario = carta_1 + carta_2
    print(f"Total: {cartas_usuario}")

    while True:
        if cartas_usuario <= 21:
            escolha = input("\nDeseja adicionar uma carta? (s/n): ").lower()
            if escolha == "s":
                carta = escolher_carta()
                cartas_usuario += carta
                
                print(f"Total: {cartas_usuario}")
                    
            elif escolha == "n":
                return(cartas_usuario)

            else:
                print("Escolha invalida")
                continue
        else:
            derrota("Dealer")
            break
         
def escolha_dealer(cartas_usuario):
    print("\nCartas do Dealer: ")
    carta_1 = escolher_carta()
    carta_2 = escolher_carta()

    cartas_dealer = carta_1 + carta_2
    print(f"Total do Dealer: {cartas_dealer}\n")

    while True:
        if cartas_dealer <= 21:
            if cartas_dealer < cartas_usuario:
                carta = escolher_carta()
                cartas_dealer += carta
                print(f"Total: {cartas_dealer}")
            elif cartas_dealer == cartas_usuario:
                print("Empate")
            else:
                print("Dealer Venceu!")
                return cartas_dealer
            
        else:
            derrota("Usuario")
            break

def derrota(vencedor):
    print(f"\nEstourou \n{vencedor} venceu!")

def continuar(vidas):

    verificar_vidas(vidas)

    print(f"\nVocê tem {vidas} vidas.")
    escolha = input("Deseja continuar? (s/n): ").lower()
    if escolha == "s":
        apagar()
        iniciar_jogo(vidas)
    elif escolha == "n":
        apagar()
        print("Obrigado por jogar!")
        sair()
    else:
        apagar()
        print("Escolha invalida")
        continuar(vidas)

def verificar_vidas(vidas):
    if vidas <= 0:
        espera(2)
        apagar()
        print("Suas vidas acabaram...")
        sair()

#--------------------------------------------------------------------------
def iniciar_multiplayer(vidas_player1 = 3, vidas_player2 = 3):
    n_rodada = 1
    vidas_player1 = vidas_player1
    vidas_player2 = vidas_player2

    while True:
        print(f"Rodada {n_rodada}")
        rodada()
        input()
        n_rodada += 1

def rodada():
    print("\nPlayer 1: ")
    cartas_player1 = escolha_inicial()
    print(f"Total do Player 1: {cartas_player1}")

    print("\nVez do Player 2: ")
    cartas_player2 = escolha_inicial()
    print(f"Total do Player 2: {cartas_player2}")

    (cartas_player1, cartas_player2) = rodadas_alternadas(cartas_player1, cartas_player2)
    print(f"Player1: {cartas_player1} "
          f"\nPlayer2: {cartas_player2}")
    
def escolha_inicial():
    carta_1 = escolher_carta()
    carta_2 = escolher_carta()
    total_cartas = carta_1 + carta_2
    print(f"Total: {total_cartas}")

    escolha = input("\nDeseja adicionar outra carta? (s/n): ").lower()
    if escolha == 's':
        total_cartas += escolher_carta()
        if estourou(total_cartas):
            
    
    return total_cartas

def rodadas_alternadas(cartas_player1, cartas_player2):
    continuar_player1 = True
    continuar_player2 = True

    while continuar_player1 and continuar_player2:
        continuar_player1 = True
        continuar_player2 = True

        if (continuar_player1):
            print("\nVez do player 1: ")
            escolha1 = input(f"\nTotal: {cartas_player1}. Deseja adicionar outra carta? (s/n): ").lower()
            if escolha1 == "s":
                cartas_player1 += escolher_carta()
                print(f"Total: {cartas_player1}")
                
            else:
                print("Player 1 passou. ")
                continuar_player1 = False


        if (continuar_player2):
            print("Vez do player 2: ")
            escolha2 = input(f"\nTotal: {cartas_player2}. Deseja adicionar outra carta? (s/n): ").lower()
            if escolha2 == "s":
                cartas_player2 += escolher_carta()
                print(f"Total: {cartas_player2}")
            else:
                print("Player 1 passou. ")
                continuar_player1 = False
    print("Os dois pularam. \n\nResultado da Rodada: ")
    return (cartas_player1, cartas_player2)

def estourou(cartas):
    if cartas > 21:
        print(f"Estourou!")
        return True
    else:
        return False


iniciar_menu()