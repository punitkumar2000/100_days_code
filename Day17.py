class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following +=1

user_1 = User("001", "Punit")
user_2 = User("002", "Mann")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


#Down below is too leanthy

# user_1 = User()
# user_1.id = "001"
# user_1.name = "Punit"

# user_2 = User()
# user_2.id = "002"
# user_2.name = "Mann"

# print(user_1.name)
# print(user_2.name)
