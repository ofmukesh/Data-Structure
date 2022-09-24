def insertionSort(arr):
  for i in range(len(arr)):
    temp=arr[i]
    j=i-1
    while(j>=0 and temp < arr[j]):
      arr[j+1]=arr[j]
      arr[j]=temp
      j-=1
  print(arr)
  
  
insertionSort([6,5,1,3,7])
