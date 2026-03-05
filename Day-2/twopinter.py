#write a code to replace all occruences of negatives numbers in a list with zero

arr= list(map(int,input("enter the elements of the list separated by space:").split()))
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print("Reverse array is: ",arr)
