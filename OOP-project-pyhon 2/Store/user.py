class User:
    def __init__(self, user_id = None, user_full_name = None, password = None, online = 0):
        self.user_id = user_id
        self.user_full_name = user_full_name
        self.password = password
        self.online = online


    def login(self, entered_password):
        if self.password == entered_password:
            self.online = 1


    def logout(self):
        print('Logged out successfully.')
        return True

    def __str__(self):
        return f"User: {self.user_full_name}\nID: {self.user_id}\nPassword: {self.password}"
