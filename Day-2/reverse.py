#traversal method
s = input("Enter a string: ")

letters = digits = special_char = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special_char += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", special_char)
