'''words = input("enter a list of words separated by spaces : ").split()
result=min(words,key=len)
print("the shortest word is: ",result)'''

"""nums = list(map(int,input("enter numbers:").split()))
result=max(nums, key=lambda x:x%10)
print(result)"""

"""nums = list(map(int,input().split()))
largest = max(nums,key =abs)
nums.remove(largest)
s1=max(nums,key=abs)
print(s1)"""

"""arr = list(map(int,input().split()))
freq={}
for x in arr:
    freq[x]= freq.get(x,0)+1
max_element=max(freq,key=lambda X:freq[x])
print(max_element)"""

"""words=["hello","World","Python","programming"]
vowels = "aeiouAEIOU"
max_count = 0
max_word = ""

for word in words:
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1

    if count > max_count:
        max_count = count
        max_word = word

print(max_word)"""

"""#easy method(implementation)

def vowels_count(word):
    return sum(1 for ch in word if ch in vowels)
words =["hello","World","Python","programming"]
vowels="AEIOUaeiou"
result=max(words,key=vowels_count)
print(result)"""

#nearer to the nearest to the target
"""arr=list(map(int,input().split()))
target=int(input())
near=arr[0]
for i in arr:
    if abs(i-target)<abs(near-target):
        near=i
print(near)"""

# write a code to find the second most repeated element
# in an array of integers

arr = list(map(int, input("Enter the array of integers: ").split()))

freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1

first = second = None

for k in freq:
    if first is None or freq[k] > freq[first]:
        second = first
        first = k
    elif second is None or freq[k] > freq[second]:
        second = k

print("Second most repeated element:", second)




