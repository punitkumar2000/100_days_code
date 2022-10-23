# new_list = [new_item for item in list]


# numbers = [1,2,3]

# new_list = []

# for i in numbers:
#     new = i + 1
#     new_list.append(new)

# print(new_list)

# new_list = [i+1 for i in numbers]
# print(new_list)


# name = "punit"
# name_list = [i for i in name]
# print(name_list)


# numbers = [i * 2 for i in range(1,5)]
# print(numbers)

names = ["punit", "mann", "python", "hii"]

new_list = [name.upper() for name in names if len(name) < 5]
print(new_list)