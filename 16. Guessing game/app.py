import math

i = 1
tries = 3
secret_number = 5
guessed = False

number = int(input("Guess the number: "))

while i <= tries and not guessed:
    
    if i != 1:        
        number = int(input("Try again: "))

    if number == secret_number:
        print("You win!")
        guessed = True
    
    if i == tries and guessed == False:
        print("You lose!")

    i += 1