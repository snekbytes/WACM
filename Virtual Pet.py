import random
#initialise values to use later
hunger=0
boredom=0
crit1=""
m="happy"
cont="yes"

#initialise a loop
while cont=="yes":
    crit1=input("What do you want to name your critter? ")
    status="alive"
    chatOptions=["Hi there!", "My name is "+crit1+"!", "I like talking to you.", "I feel "+m+"!"]

#initialise the game loop; check the critter is still alive
    while status=="alive":
        if boredom<0:
            boredom=0
        if hunger<0:
            hunger=0
        option=input("What would you like to do? \n [1] Talk \n [2] Feed \n [3] Play \n [4] Check Status \n")
#run the relevant code with eaech option
        if option=="1":
            boredom -=1
            choice=random.randint(0,3)
            print(chatOptions[choice])
            hunger+=1
            
        elif option=="2":
            hunger-=1
            print("Mmmmmmm yummy!")
            boredom+=1
                        
        elif option=="3":
            boredom-=1
            print("I'm having so much fun!")
            hunger+=2
            
        elif option=="4":
            print("Hunger Level: "+str(hunger)+"\nBoredom Level: "+str(boredom)+"\nMood: "+m)
            boredom+=1
            hunger+=1
            
        else:
            print("\""+option+"\" is not a valid input, please try again.")
#check its not dead, if it is, exit          
        unhappiness=hunger+boredom
        if unhappiness <=5:
            m="happy"
        elif unhappiness <=10:
            m="okay"
        elif unhappiness <=15:
            m="sad"
        elif unhappiness <=20:
            m="mad"
        else:
            status="dead"
#option to restart if the critter dies   
    cont=input("Oh no! "+crit1+" died! \nWould you like to make another pet? ")
    cont=cont.lower()
