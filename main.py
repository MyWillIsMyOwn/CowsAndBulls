import random
import sys

def generator():
    return str(random.randint(1000,9999))

def compare (user_number,generated_number):
    cow = 0
    bull = 0
    for _ in range(len(generated_number)):
        if user_number[_]==generated_number[_]:
            cow +=1
        else:
            bull +=1
    return cow, bull

def playagain():
    answer = input("Wanna play again? y/n")
    if(answer=="y"):
        game()
    else:
        sys.exit()

def game():
    generated_number = generator()
    print(generated_number)
    while True:
        user_number = input("Try to guess the 4-dig number...")
        while len(user_number)!=4:
            user_number = input("Try to guess the 4-dig number...")
        cowsandbulls = compare(user_number, generated_number)

        if cowsandbulls[0] == 4:
            print(
                "Congratulations, you got all " + str(cowsandbulls[0]) + " cows and " + str(cowsandbulls[1]) + " bulls")
            playagain()
        else:
            print("Try again, you got only " + str(cowsandbulls[0]) + " cows and " + str(cowsandbulls[1]) + " bulls")

generate = input("Do you want to genrate number? y/n")

if generate=="y":
    game()
else:
    sys.exit()










