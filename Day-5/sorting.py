#sort characters in a string

"""s=input("enter a string : ")
sorted_char=sorted(s)
print("".join(sorted_char))"""

#built in sort

"""words= input("enter words:").split()
words.sort(reverse=True)
print(words)"""

#write a code to sort string manually without any sort?sorted inbulit
#functions or methods
"""s=input("enter a string : ")
arr=list(s)
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("".join(arr))"""

#sort with length

"""words=input("enter languages : ").split()
words.sort(key=len,reverse=True)
print(words)"""


