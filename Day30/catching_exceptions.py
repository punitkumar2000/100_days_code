# FileNotFound
# with open("file.txt") as f:
#     file = f.read()

# KeyError
# dictionary = {"key":"value"}
# value = dictionary["non_existing_key"]

# IndexError
# fruits = ["Aple", "Banana", "Pear"]
# fruit = fruits[3]

# TypeError
# text = "abc"
# print(text + 0)


#-------------------------------------------------------------
# try:
#     file = open("file.txt")
#     dictionary = {"key":"value"}
#     print(dictionary["key"])
# # except FileNotFoundError:
# #     file1 = open("Day30/new_file.txt", "w")
# #     file1.write("Something")
# except KeyError as error_messege:
#     print(f"The key {error_messege} does not exists")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up")

#-------------------------------------------------------------
# Index error handling
# fruits = ["Apple", "Pear", "Orange"]

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + "Pie")

# make_pie(3)

#-------------------------------------------------------------
# Key Error handling
facebook_posts = [
{'likes':21, 'Comment':2},
{'likes':13, 'Comment':2, 'Shares':1},
{'likes':1, 'Comment':2}
]
total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['likes']
        # print(total_likes)
    except KeyError:
        if "like" not in facebook_posts:
            post["likes"] =0
            total_likes += post["likes"]
            # print(total_likes)
print(total_likes)
    