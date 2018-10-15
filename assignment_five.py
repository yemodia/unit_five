import random

def user_play():
    while True:
        want_play = input("Do you want to play?")
        if want_play == "y" or want_play == "n":
            break
    return want_play

def random_number():
    number = random.randint (1,100)
    return number



def main():
    while True:
        if user_play() == "y":
            answer = random_number()
        user_guess = input("Pick a number between 1 and 100:")
        if user_guess == random_number():
            print("You guessed it")
            break

        else:
            print("Ok, see you later")

            if user_guess <=1  and user_guess <= 100:
                


main()
