import random

target = random.randint(1 , 100)

print(" Welcome to the Game, Guess the number!")
print(" You have to guess a number between 1 to 100")
while True:
    userChoice = int(input("Guess the number or Quit : "))
    if(userChoice == " Quit"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print( "Success : Correct Guess !! ")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess..")
    else:
        print("your number was too big. Take a smaller guess")

print ( "--------GAME OVER--------")
