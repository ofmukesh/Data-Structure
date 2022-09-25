arr=[4,5,34,58,1,5]

for i in range(len(arr)-1,0,-1):
    temp=arr[i]
    if temp<arr[i-1]:
        arr[i]=arr[i-1]
        arr[i-1]=temp
print(arr)
