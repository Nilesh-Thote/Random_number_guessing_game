
import random
range=input("The range starts from 0 to " ": ")
try:
    if range.isnumeric():
        range=int(range)
except:
    print("Enter Numbers only")
    quit()
random_no_generator=random.randint(0,range)
chance=int(input("Enter how many chances do you want to guess the no"))
answer=int(input("Guess the number"))
count=0
while True:
    if answer==random_no_generator:
        print("Congratulation you won!\nyou have guessed the number")
        break
    elif answer<random_no_generator:
        print("the guess number is low")
    else:
        print("the guess number is high")
    answer=int(input("Guess the Number"))
    count+=1
    if count==chance:
        print("you lose, The correct no was" +str(random_no_generator))
        break