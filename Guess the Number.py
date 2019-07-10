# Using a divide an conquer strategy, the computer will guess an input number.
# When found, it displays how long it took. 

num=input("Input a number between 1 and 10000 for the computer to guess.\n")
while True:
    #check that the number input is a) a number, and b) between the bounds
    #if not, loop until both conditions are met. 
    try:
        num=int(num)
        if num>1000 or num<0:
            num=input("Invalid input. Your number is out of bounds.\n")
        else:
            break
    except ValueError:
        while not(num.isnumeric()):
            num=input("Invalid input. You did not type a number.\n")

# set initial boundaries
top=10000
bottom=0
count=1
guess=5000

# while still guessing, loop through, setting the guess to either the upper or
# lower bound, depending if the number is higher or lower than the guess. 
while guess!=num:
    if num>guess:
        bottom=guess
    else:
        top=guess
    #new guess is the halfway point between the top and bottom bounds
    guess=round((top+bottom)/2,0)
    count+=1
    print(guess)
print("It took the computer ", count," tries to guess your number.")
