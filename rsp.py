import random

liste=["AI "] #AI conversations

liste2=[" "] #Player conversations


def play():
    user=input("what would you like to choose? for rock 'r',for scissors 's' , for paper'p'") 
    computer = random.choice(['r','p','s'])
    
    pc = random.choice(liste)
    ll= random.choice(liste2)
    
    if user == computer:
        print("similar") #if both sides are same
    
    #r > s , s > p , p > r
    if is_win(user, computer):
        return ll
    
    return pc

def is_win(player, opponent):
    #return true if player wins
    if(player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        return True
    

print(play())