class User:
    # __init__ is a constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.name = "Talib"
# user_1.id = "001"
user_1 = User("Talib", "001")
user_2 = User("ALi", "002")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
