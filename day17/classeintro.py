class User:

    def __init__(self, username, user_id):

        print("user created")
        self.username = username
        self.user_id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        #the user that is passed in has its followers increased by 1
        self.following += 1
        #the user that has chosen to follow the user passed in has their following increased by 1


user_1 = User("Chris", "001")
user_2 = User("Jenny", "002")

user_1.follow(user_2)
print("User_1 stats", user_1.followers, "followers...", user_1.following, "following....")
print("User_2 stats", user_2.followers, "followers...", user_2.following, "following....")
