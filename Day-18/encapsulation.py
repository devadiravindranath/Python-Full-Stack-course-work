class Snapchat:
    def __init__(self,username,password,friends):
        self.username=username
        self.__password = password #
        self._friends = friends

    def getpassword(self):
        return self.__password

    def setpassword(self,new_password):
        self.__password = new_password

    @property
    def oprFriends(self):
        return self._friends

    @oprFriends.setter
    def oprFriends(self,newfriend):
        self._friends.append(newfriend)

    

        
dileep = Snapchat('dileep','123456',['abid','ravi'])

print(f'Name before modification: {dileep.username}')

dileep.username='vicky'
print(f'Name after modification: {dileep.username}')


print(f'Name before modification: {dileep.getpassword()}')

dileep.setpassword('99999')
print(f'Password after modification: {dileep.getpassword()}')

print(f'Friends before modification: {dileep.oprFriends}')

dileep.oprFriends='uday'
print(f'Friends after modification: {dileep.oprFriends}')



