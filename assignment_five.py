# Yerim Dia
# October 18, 2018
# Introduction to Computer Science
# This program is under the form of a game.
# It asks the user if they ant to play. If they choose no, the program ends.
# O=If they choose yes, the program generates a random number and asks the user to guess.
# According to the number the user inputs, it will display if the guss was too high or too low.
# Once the user finds the answer, the program will tell them in how many guesses they found it.
# The program will then ask the user if they want to play again. If they say no, the program will end.
# And if they say yes, the program will start again with a new number.

import random


def user_play():
    """
    This function gets input from the user regarding if they want to play or not
    :return: It returns the user's response
    """
    while True:
        want_play = input("Do you want to play?")
        if want_play == "y" or want_play == "n":
            break
    return want_play


def random_number():
    """
    This function generates a random number tha the user will have to guess
    :return: It returns the random number to the main function
    """
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
