# Scopes

# fruits = 10             #Global variable
# def fruits_total():
#     fruit = 20          #Local variable
#     print(fruit)
#     print(fruits)
# fruits_total()
# print(fruits)

#There is no block scope

# game_level = 3
# def enemies():
#     enemies = ["Zombie", "Skeleton", "alien"]
#     if game_level < 5:
#         new_enemies = enemies[0]
#
#     print(new_enemies)
# enemies()


#Modifying Global scope

# fruits = 10
# def no_of_fruits():
    # fruits = 20
    # global fruits
    # fruits += 10
    # print(fruits)
    # return fruits + 1


# fruits = no_of_fruits()
# print(fruits)

#Constants and Global Scope
# PI = 3.14
# URL = "www.google.com"
#
# def func():
#     name = "Punit"


#Guess the number
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0


def check_answer(answer, guess, turns):

    if answer < guess:
        print("Too High")
        return turns - 1

    elif answer > guess:
        print("Too Low")
        return turns - 1
    else:
        print(f"You Got it, The answer was{answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type easy or hard:")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    answer = randint(1,100)
    print(answer)

    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} no of attempts to guess the game:")
        guess = int(input("Guess the number"))
        turns = check_answer(answer, guess, turns)
        if guess == 0:
            print("You run out of guesses, You loose!")
            return
        elif guess != answer:
            print("Guess Again!")

game()


