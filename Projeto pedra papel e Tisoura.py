import random
import os


move_list = ["papel", "pedra", "tesoura"]
player_count = 0
computer_count = 0

print("==============")
print("Bem vindo ao Jogo Papel, Pedra e Tesoura")

def main_print(): 
    print("==============")
    print("\nPLACAR:")
    print("Você: {}". format(player_count))
    print("Computador: {}". format(computer_count)) 
    print("\n")
    print("Escolhe seu lance:")
    print("0 - Papel | 1 - Pedra | 2 - Tesoura")

def select_move():
    return random.choice(move_list)

def get_player_move():
    while True: 
        try: 
            player_move = int(input())
            if player_move not in [0, 1, 2]: 
                raise
            return move_list[player_move]

        except Exception as e: 
            print(e)

def select_winner(p_move, c_move):
    global player_count, computer_count

    if p_move == "papel": 
        if c_move == "pedra":
            player_count += 1
            return "p"
        
        elif c_move == "tesoura":
            computador_count +=1
            return "c"
        
        else: 
            return "d"
        
    if p_move == "pedra": 
        if c_move == "tesoura":
            player_count += 1
            return "p"
        
        elif c_move == "papel":
            computador_count +=1
            return "c"
        
        else: 
            return "d"
        
    if p_move == "tesoura": 
        if c_move == "papel":
            player_count += 1
            return "p"
        
        elif c_move == "pedra":
            computador_count +=1
            return "c"
        
        else: 
            return "d"
again = 1
while again == 1: 
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)

    print("")
    print("====================")
    print("Sua Jogada: {}".format(player_move.upper()))
    print("Computador Jogada: {}".format(computer_move.upper()))

    if winner == "p": 
        print("Você ganhou!")
    elif winner == "c": 
        print("Computador ganhou!")
    else: 
        print("Empate!")
    print("====================")

    while True: 
        print("Jogar Novamente? 0 - SIM | 1 - Não")
        next = int(input())
        if next == 0: 
            break
        elif next == 1:
            again = 0
            break

    os.system("clear")