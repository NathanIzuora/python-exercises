#name = input("WHAT IS YOUR NAME?")
#print("HELLO", name.upper())
#print("YOUR NAME HAS", len(name), "LETTERS IN IT!")


#names = input("What is your name?")
#color = input("What is your favorite color?")
#print("Youre name is", names , ". And your favorite color is" , color ,"!")

# guessing game
# secret_number= int(input("Guess the number"))
# while secret_number == 5:
#    print("Correct!")
#    break
#else:
#    print("Try again")
#secretnum = 5
#theguess = int(input("Guess a number between 1 and 10"))
#while True:
   # if theguess == 5:
    #    print("Yups")
    #    break
    #elif theguess < 5:
     #   print(theguess , "is too small")
   #     break
    #elif theguess > 5:
     #   print(theguess , "is too high")
    #    break
    #elif theguess > 10:
    #    print("this number is not allowed")
    #    break

import random

secret_number = random.randint(1, 10)
print('I am thinking of a number between 1 and 10.')
while True:
    guess = int(input("What's the number? "))
    if guess == secret_number:
        print('Yes! You win!')
        break
    elif guess < secret_number:
        print('Too high. Try again.')
    elif guess > secret_number:
        print('Too low. Try again.')
    else:
        print('Nope, try again.')
