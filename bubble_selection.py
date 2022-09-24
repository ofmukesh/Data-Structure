def selectionBubbleSort(arr):
  for i in range(len(arr)):
      minn=arr[i]
      mini=0
      for j in range(i,len(arr)):
          if minn>=arr[j]:
              minn=arr[j]
              mini=j
      arr[mini]=arr[i]
      arr[i]=minn
  print(arr)
selectionBubbleSort([3,2,1])
