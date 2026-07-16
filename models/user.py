class User:
    
    def __init__(self, user_id, username, password, role):

        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def display_user(self):

        print("User ID :", self.user_id)
        print("Username :", self.username)
        print("Password :", self.password)
        print("Role :", self.role)