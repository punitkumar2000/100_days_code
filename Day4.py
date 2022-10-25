# Head or tail program

# import random
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Head")
# else:
#     print("Tail")

# picking up the random from the list
# import random
# names = ["punit", "ram", "shyam"]
# random_name = random.choice(names)
# print(f"{random_name} is going to buy the meal today!")


#Nested list into another list

# names_1 = ["ram", "shyam"]
# names_2 = ["bharat","krishna"]
#
# new_lists = [names_1, names_2]
# print(new_lists)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1])

#Who will pay the bill
# import random
# names_string = input("Please enter the names:")
# names = names_string.split(", ")
# name_len = len(names)
# random_name = random.randint(0, name_len - 1)
# person = names[random_name]
# print(f"{person} will have to pay the bill")

#treasure map
# row1 = [" "," "," "]
# row2 = [" "," "," "]
# row3 = [" "," "," "]
#
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where you want to put your treasure:")
# horizontal = int(position[0])
# vertical = int(position[1])
#
# map[horizontal - 1][vertical - 1] ="X"
# print(f"{row1}\n{row2}\n{row3}")



#Rock Paper scissor
# import random
# user_choice = int(input("Choose 0 for rock, 1 for paper and 2 for scissor:"))

# if user_choice >= 2 or user_choice < 0:
#     print("You types a invalid number, You loose!")
# else:
#     computer_choice = random.randint(0, 2)
#     print(f"Computer choose:{computer_choice}")
#
#     if user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You loose!")
#     elif computer_choice > user_choice:
#         print("You loose!")
#     elif user_choice > computer_choice:
#         print("You win!")
#     elif user_choice == computer_choice:
#         print("Its a draw!")
