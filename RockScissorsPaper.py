import random

def play():
    user = input("what is your choice? 'r' for rock, 'p' for paper , 's' for scissors \n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'its a tie'

    if is_win(user,computer):
        return 'you won!'     

    return 'you lost!'    

def is_win(player,opponent):
    if (player == 'r' and opponent== 's') or ( player == 's' and opponent == 'p') or (player == 'p' and opponent== 'r'):
        return true
