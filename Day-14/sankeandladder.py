import random
import sys




player_1 = input("Enter the player-1 name : ").title()
player_2 = input("Enter the player-2 name : ").title()

player1_score,player2_score=0,0 #intial position
winning_point=100

snakes={16:7, 22:14, 34:9, 59:20, 67:37, 79:10, 90:18 }
ladders={8:30, 17:28, 46:90, 56:70,}

def dice():
    return random.randint(1,6)

def player1_turn():
    global player1_score
    player1_status= input(f"(Player_1), You Want To [c]ontinue or [q]uit: ").lower()
    if Player1_status=='c':
        cur_dic=dice()
        print(f'Dice: {cur_dic}')
        Player1_score+=cur_dic
        if player1_score>winning_point:
            sys.exit()

        if Player1_score in snakes:
            Player_score=snakes[Player1_score]
            print(f'Board position after snake bit: {Player1_score}--------')
        elif Player1_score in ladders:
            Player_score1 = ladders[Player1_score]
            print(f'Board position after ladder: {Player1_score}######')
        else:
            print(f'Board position: {Player1_score}')
    else:
        print(f'congrats {Player_2},You won the Game!!!')

def player2_turn():
    global player2_score
    player2_status= input(f"(Player_2), You Want To [c]ontinue or [q]uit: ").lower()
    if Player2_status=='c':
        cur_dic=dice()
        print(f'Dice: {cur_dic}')
        Player2_score+=cur_dic
        if player2_score>winning_point:
            sys.exit()

        if Player2_score in snakes:
            Player_score=snakes[Player1_score]
            print(f'Board position after snake bit: {Player2_score}--------')
        elif Player2_score in ladders:
            Player2_score = ladders[Player1_score]
            print(f'Board position after ladder: {Player1_score}######')
        else:
            print(f'Board position: {Player1_score}')
    else:
        print(f'congrats {Player_1},You won the Game!!!')

while Player1_score<winning_point and Player2_score<winning_ponit:
    Player1_turn()
    Player2_turn()

if Player1_score>Player2_score:
    print(f'congrats {Player_1},You won the Game!!!')
else:
    print(f'congrats {Player_2},You won the Game!!!')
        
            



                  
            
