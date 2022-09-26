no=int(input())
arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
row=-1
col=-1
for i in range(len(arr)):
    k=len(arr)-1-i
    for j in range(len(arr[i])):
        if arr[i][j]==no:
            row=i
            col=j
            break
        if arr[k][j]==no:
            row=i
            col=j
            break
    if row != -1 and col!= -1:
        break
print(row,col)
