0# for loop

# fruits = ["Apple", "Banana", "Cherry"]
# for fruit in fruits:
#     print(fruit)
#     print(fruits)
# print(fruits)

#Total average height

# student_heights = input("enter a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#
# total_height = 0
# for height in student_heights:
#     total_height += height
# # print(total_height)
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# # print(number_of_students)
#
# average_height = total_height / number_of_students
# print(round(average_height))


#Highest score
# student_scores = input("Enter the student scores:").split()
# for n in range(0 ,len(student_scores)):
#     student_scores[n] = int(student_scores[n])
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The Highest score in the class is {highest_score} ")

# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#     if score > student_scores:
#         highest_score = score
# print(f"The highest score in the class is {highest_score}")


#Total sum between 0 - 100 only (even number)
# total_sum = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total_sum += number
# print(total_sum)

#### OR ####
# total_sum = 0
# for number in range(2, 101, 2):
#     total_sum += number
# print(total_sum)

#Print fizz(multiple of 3) buzz(multiple of 5) and both fizz buzz (both multiple of 3 and 5)

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Buzz")
#     elif number % 5 == 0:
#         print("Fizz")
#     else:
#         print(number)

# Password generator
import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Easy way
# password = ""
# print("Welcome to PyPassword generator!")
# number = int(input("How many number would you like:"))
# letter = int(input("How many letter you want in your password"))
# symbol = int(input("How many symbol you want in your password:"))
#
# for char in range(1, number + 1):
#     password += random.choice(numbers)
# for char in range(1, letter + 1):
#     password += random.choice(letters)
# for char in range(1, symbol + 1):
#     password += random.choice(symbols)
# print(password)

#hard level
# password_list = []
# print("Welcome to PyPassword generator!")
# number = int(input("How many number would you like:"))
# letter = int(input("How many letter you want in your password"))
# symbol = int(input("How many symbol you want in your password:"))
#
# for char in range(1, letter + 1):
#     password_list.append(random.choice(letters))
# for char in range(1, symbol + 1):
#     password_list += random.choice(symbols)
# for char in range(1, number + 1):
#     password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)


