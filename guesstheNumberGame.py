#guess the Number game
import random
#using num as variable to get random number from the impoted file
num=random.randint(1,10)
attempt =0
#Taking input from user
guess=int(input("can you guess the number Iam thinking ?  it is less than 10=" ))

while num !=guess:
    if guess>num:
              print("you guess is higher")

    else:
            print("your guess is lower")
            #increasing the attempt
            attempt+=1
            print("your attempt is " , attempt)
            #to cotinue the game taking input once again
            guess=int(input("guess again="))
    if attempt<3:
        print("you lose game")
        exit()
   #if user input match with the num
print("you won!!")