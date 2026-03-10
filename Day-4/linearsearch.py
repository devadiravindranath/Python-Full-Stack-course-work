'write a code to search an element by linear approach'

arr= list(map(int,input("enter elements with spaces :").split()))
key=int(input("enter element to be searched :"))
found=False
for i in range(len(arr)):
    if arr[i]==key:
        print("element found at index",i)
        found =True
        break
if not found:
    print("element not found") 
