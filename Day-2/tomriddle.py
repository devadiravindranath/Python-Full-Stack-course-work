# Program to check Tom Riddle anagram (ignoring spaces & case)

s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are NOT anagrams of each other.")
