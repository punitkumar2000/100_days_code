# Write a program to check someone can ride the roller coaster as per 120 cm height

# bill = 0
# print("Welcome to the roller coaster!")
# height = int(input("please enter your height:"))
#
# if (height >= 120):
#     age = int(input("What is your age:"))
#
#     if age < 12:
#         bill = 5
#         # print("Please pay $ 5 ")
#
#     elif age > 12 and age < 18:
#         bill = 7
        # print("Please pay $ 7")

#     else:
#         bill = 12
# #         # print("Please pay $ 12")
#
#     photo = input("Do you want photoes? (y/n)").lower()
#     if photo == "y":
#         bill += 3
#     print("GO and enjoy the ride!")
#     print(f"{bill} is your final bill ")
#
# else:
#     print("Sorry, You have to grow taller before ride!")


# BMI calculator 2
# height = float(input("please enter your height in m: "))
# weight = int(input("Please enter your weight in kg: "))

# BMI = round(weight / height ** 2)
# print(BMI)
#
# if BMI < 18.5:
#     print("underweight")
# elif BMI > 18.5 and BMI < 25:
#     print("normal weight")
# elif BMI > 25 and BMI < 30:
    # print("over weight")
# elif BMI > 30 and BMI < 35:
#     print("obese")
# else:
#     print("clinically obese")

# WAP tp check the year is leap year or not
# year = int(input("Enter the year which your want to check: "))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#     print("leap year")
# else:
#     print("Not a leap year")


# pizza order

# Bill = 0
# print("Welcome to the pizza hut")
# Pizza_size = input("What size of pizza you want?(s/m/l):").lower()
#
# if Pizza_size == "s":
#     Bill = 15
# elif Pizza_size == "m":
#     Bill = 20
# elif Pizza_size == "l":
#     Bill = 25
#
# Peproni = input("Do you want peproni topping?(y/n):").lower()
#
#
# if Peproni =="y":
#     if Pizza_size == "s":
#         Bill += 2
#     else:
#         Bill +=3
# Extra_cheese = input("Do you want extra cheese?:(y/n)").lower()
# if Extra_cheese =="y":
#     Bill += 1
# print(f"Your total bill is ${Bill} ")

# Love calculator

# print("Welcome to the love calculator")
# name1 = input("Please enter your name: ").lower()
# name2 = input("Please enter your patner name: ").lower()
#
# combined_names = name1 + name2
#
# t = combined_names.count("t")
# r = combined_names.count("r")
# u = combined_names.count("u")
# e = combined_names.count("e")
# true = t + r + u + e
#
# l = combined_names.count("l")
# o = combined_names.count("o")
# v = combined_names.count("v")
# e = combined_names.count("e")
# love = l + o + v + e
#
# love_score = int(str(true) + str(love))
# # love_score = 45
# print(love_score)
#
# if love_score < 10 or love_score > 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score > 40 and love_score < 50:
#     print(f"Your score is {love_score}, you are already together.")
# else:
#     print(f"Your score is {love_score}.")


# Treasury Game
# print("Welcome to the game!")
# path = input("Which path you want to choose L/R:").lower()
#
# if path == "l":
#     print("Hooray You clear your first level")
#
#     water = input(
#         "Do you want to wait for the boat or you want to reacher the island by swiming ..... choose w for wait and s for swim:").lower()
#
#     if water == "w":
#         print("Hooray You clear your second level")
#
#         door = input("Please choose the door").lower()
#         if door == "y":
#             print("hooray..... You won the game!!!!")
#         else:
#             print("Game over..... Please play again!!!!!")
#
#     else:
#         print("Game over..... Please play again!!!!!")
#
# else:
#     print("Game over..... Please play again!!!!!")










