import random

def play():
    user = input("What's your choice ?? 'r' for rock, 'p' for paper or 's' for scissors : ")
    comp = random.choice(['r', 'p', 's'])
    print(f"computer choose {comp} ")

    if user == comp:
        return "it's a tie"

    if is_win(user, comp):
        return "You Win"
    return "You Lost"

    

def is_win(player, opponent):

    if (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's'):
        return True

print(play())
    