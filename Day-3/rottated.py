arr= list(map(int,input("enter nums with space:").split()))
first=arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[-1]=first
print("rotated arr:",arr)
