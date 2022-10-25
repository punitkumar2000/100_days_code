# Squaring numbers
# listt = [1,2,3]

# new_list = [square * square for square in listt]
# print(new_list)


#Filtering even numbers
# listt = [1,2,3,4,5,6,7,8,9]

# new_list = [nums for nums in listt if nums % 2 == 0]
# print(new_list)


# Data over lap problem

with open("Day26/file1.txt") as file1: 
    file1_data = file1.readlines()

with open("Day26/file2.txt") as file2:
    file2_data = file2.readlines()

result = [num for num in file1_data if num in file2_data]
print(result)
