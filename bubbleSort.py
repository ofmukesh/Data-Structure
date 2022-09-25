arr=[4,5,34,58,1,5]

# bubbling smallest no. to the top

for i in range(len(arr)-1,0,-1):
    temp=arr[i]
    if temp<arr[i-1]:
        arr[i]=arr[i-1]
        arr[i-1]=temp
print(arr)

# sorting array

for i in range(len(arr)):
    for j in range(len(arr)-1,i,-1):
        temp=arr[j]
        if temp<arr[j-1]:
            arr[j]=arr[j-1]
            arr[j-1]=temp
print(arr)
