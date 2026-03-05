'''write a code to find the second largest element in an array by using one pass'''

arr=list(map(int,input("enter the elements with space: ").split()))
largest= -10**9
second = -10**9
for num in arr:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        second = num
print("second largest element is: ",second)
