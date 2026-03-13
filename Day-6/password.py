password = input("Enter the Password: ")

if len(password)>=8:
    s=set()
    for i in password:
        if i.isupper():
            s.add("upper")
        elif i.islower():
            s.add("lower")
        elif i.isdigit():
            s.add("digit")
        else:
            s.add("special character")
    if len(s)==4:
        print("strong password")
    else:
        print("weak password . Password needs to have upper,lower,special character and digit")
else:
    print("length needs to be =>8")
