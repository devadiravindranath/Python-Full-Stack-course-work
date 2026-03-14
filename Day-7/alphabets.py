"""ch =65
for i in range(1,27):
    for j in range(i):
        if ch<=90:
            print(chr(ch),end=" ")
            ch+=1
    print()"""

"""s= input("Enter a string: ")
for i in range(len(s)):
    print(" ".join(s[:i+1]))
for i in range(len(s)-1,0,-1):
    print(" ".join(s[:i]))"""

#rotate string
"""s1=input("enter the string: ")
k=int(input("enter the number of characters to rotate: "))
for i in range(k):
    s1=s1[-1]+s1[:-1]
print('rotated string: ',s1)"""
#count letter
"""
s=input("enter a string: ")
occurance={}
for char in s:
    if char in occurance:
        occurance[char]+=1
    else:
        occurance[char]=1
print("occurance of characters in the string:")
for char,count in occurance.items():
    print(f'{char}:{count}')
"""

s= input("enter the string:")
seen=set()
start=0
max_length=0
for end in range(len(s)):
    while s[end] in seen:
        seen.remove(s[start])
        start+=1
    seen.add(s[end])
    max_lenth=max(max_length,end-start+1)
print("length of longest substring: ",max_length)
