import random

number = random.randint(0,10)

guess=int(input("i'm thinking about number between 0 and 10,can you guess it."))

while True:
    if guess == number:
        print("welldone,you guess correctly,i'm thinking about", number)
        break
    else:
        guess = int(input("nope,try again : "))
play =input("press to exit ': ")
exit



           
           


