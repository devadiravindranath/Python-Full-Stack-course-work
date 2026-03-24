class amazon:
    discount = 20

    @classmethod
    def updatediscount(cls,newdiscount):
        cls.discount = newdiscount

        
    def userinfo(self,name,phonenumber):
        self.name = name
        self.phonenumber = phonenumber
        print(f'Username: {self.name}')
        print(f'Phone number: {self.phonenumber}')

    @staticmethod
    def banner():
        print("Welcome to the Amazon\n20% discount is going on ,shopp noww!!!!")



abid = amazon()
abid.userinfo("abid",123456789)

abid.updatediscount(40)
amazon.updatediscount(50)

abid.banner()
amazon.banner()

abid=amazon()


