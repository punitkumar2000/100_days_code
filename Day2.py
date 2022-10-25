# Tip Calculator

# Bill = int(input("enter the total bill: \n"))
# tip_per = int(input("At what % you would like to give 10,12 or 15:"))
# Customer = int(input("enter the total no of people: \n"))
#
# Total_bill_with_Tipp = tip_per/100 * Bill + Bill
# Bill_per_person = Total_bill_with_Tipp / Customer
# Total_Tip = tip_per/100 * Bill
#
# print("Total Bill:" + "$" , Total_bill_with_Tipp)
# print("Total Bill for per person:" + "$" , Bill_per_person)
# print("Total Tip you gave:" + "$" , Total_Tip)

# WAP to enter a 2 digit no and add that no
# n = input("Enter your 2 digit no:")
#
# first_digit = n[0]
# print(first_digit)
# second_digit = n[1]
#
# Sum = int(first_digit) + int(second_digit)
# print("Your two digit no sum is:", Sum)

#Using height and weight calculate BMI

height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

BMI = (weight) / (height ** 2)
print("Your body mass index is:",BMI)

#Rounding the digits
# print(round(1.264/2, 4))



from calendar import month

# age = int(input("Enter your age: "))
#
# year_left = 90 - age
# print("Years left:", year_left)
#
# days_left = age * 365
# week_left = age * 52
# month_left = age * 12
# print(f"You have {days_left} days, {week_left} weeks, and {month_left} months left")
# print(message)