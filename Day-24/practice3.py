class user:
    def __init__(self, username, password, otp):
        self.username = username
        self.__password = password
        self._otp = otp

    def get_password(self):
        return "******"

    def set_password(self,new_password):
        if len(new_password) < 6:
            print("Erroe:password must be 6 characters long.")
    
        else:
            self.__password = new_password
            print("password update successfully.")

    def get_otp(self):
        return self._otp
    
    def set_otp(self,new_otp):
        self._otp = new_otp
        print("otp successfully")

user1 = user("john_doe", "secure123", "123456")

print(user1.username)
user1.username = "jane"
print(user1.username)

print(user1.get_otp())
user1.set_otp("5555")
print(user1.get_otp())

print(user1.get_password())
user1.set_password("new12")
