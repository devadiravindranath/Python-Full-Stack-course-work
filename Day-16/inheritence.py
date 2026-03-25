class Instagram:
    def __init__(self,username):
        self.username = username
        print(f"hey  !! {self.username},welcome to the Instagram!!!!!!")

    def reels(self):
        print("You can upload and scoroll the reels")

    def post(self):
        print("you can post your pictures")


        

class InstagramV2(Instagram):
    def __init(self,username):
        super(). __init__(username)# calling the function 

    def story(self):
        print("you can upload your story")


class InstagramV3(InstagramV2):
    def __init(self,username):
        super(). __init__(username)# calling the function 

    def note(self):
        print("you can upload a note")

class Live:
    def Launchlive(self):
        print("Now you can go on live")

class Verification:
    def Verify(self):
        print("you can veify your account ")

class InstagramV4(InstagramV3,Live,Verification):
    def __init(self,username):
        super(). __init__(username)

class Creator(InstagramV4):
    def __init(self,username):
        super(). __init__(username)

    def insights(self):
        print("you can check your  post insights")

class Business(InstagramV4):
    def __init(self,username):
        super(). __init__(username)

    def buttons(self):
        print("you can contact them mail and number")

class InstagramV5(Creator,Business):
    def __init(self,username):
        super(). __init__(username)

        
    

nani = InstagramV5('nani')
nani.reels()
nani.post()
nani.story()
nani.note()
nani.Launchlive()
nani.Verify()
nani.insights()
nani.buttons



