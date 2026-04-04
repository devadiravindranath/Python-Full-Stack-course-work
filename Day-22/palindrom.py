import csv

def ispalindrom(n):
    rev = n[::-1]
    if n == rev:
        return "palindrom"
    else:
        return "not a palindrom"


with open("palintc.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        num = row['input']
        result = ispalindrom(num)

        if result == "palindrom":
            print(num, "Test Case Passed")
        else:
            print(num, "Test Case Failed")
