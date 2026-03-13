name = input("Entraer the name: ")
dob = input("Enter the dob[YYYY-MM-DD]: ")

username= name[1:4]+name[-3]+dob[-2:]+dob[2:4]
print(f"{name} !!!\nYour username:{username}")
