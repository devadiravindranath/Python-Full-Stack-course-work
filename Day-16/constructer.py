
#A **constructor** is a special method (`__init__`) that is **automatically called when an object is created to initialize its data**.

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f"hey  !! {self.username},welcome to the Instagram!!!!!!")

dileep = Instagram('dileep','420')
