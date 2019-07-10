import cardGamePackage

#initialise variables
cont=True
p1wins=0
p2wins=0

print("Welcome to the Game of War\n")
player1=input("What is player 1's name?\n")
player2=input("Welcome "+player1+"!\n\nWhat is player 2's name?\n")
print("Welcome "+player2+"! \n")

while cont==True:
    #do the game mechanics
    print("\nBegin!\n")
    deck=cardGamePackage.Deck()
    hand1=deck.deal()
    hand2=deck.deal()
    print(player1+": "+hand1.str())
    print(player2+": "+hand2.str())
    
    #calculate winner
    if hand1.isBetter(hand2):
        print(player1+" wins!")
        p1wins+=1
    else:
        print(player2+" wins!")
        p2wins+=1
    print("\nScoreboard: \n     "+player1+": "+str(p1wins)+
          "\n     "+player2+": "+str(p2wins))
    choice=input("\nWould you like to play again? [Y] or [N]\n")
    if choice!='Y':
        cont=False
