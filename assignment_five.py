import random


def user_play():
    while True:
        want_play = input("Do you want to play?")
        if want_play == "y" or want_play == "n":
            break
    return want_play


def random_number():
    number = random.randint(1, 100)


    return number

def main():
    while True:
        if user_play() == "y":
            answer = random_number()
            total_guess = 0

            while True:

                user_guess = int(input("Pick a number between 1 and 100:"))
                total_guess += 1
                if user_guess >= 1 and user_guess <= 100:
                    if user_guess > answer:
                        print("The guess is too high")
                    elif user_guess < answer:
                        print("The guess is too low")
                    elif user_guess == answer:
                        print("Congratulations you found the answer in", total_guess, "guesses")
                        break

        else:
            print("See you later")
            break


main()
