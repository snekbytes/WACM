import cardGamePackage
import random

while True:
    try:
        n = int(input("How many players are there?\n"))   #test if they input a number
        if n<2:
            print("Not enough players.\nPlease try again.")
        break
    except ValueError:
        print("The value inputted was not a number.\nPlease try again. ")

names=[]
for i in range(1,n+1):
    name=input("What is the name of player "+str(i)+"?\n")
    names.extend(name)
    
print("\nLet the game begin!\n")

deck=Deck()

for i in range(1,n+1):
    x=random.randint()

# Remeber for later: Hands linked to Players via dict might be a good idea
# Initialise the hands to pull only 2 cards and the hand only interacts with card object ince per game
# war will only use two cards per game so its a good idea
# GG EZ
    
