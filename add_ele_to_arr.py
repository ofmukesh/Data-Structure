ex_array=[1,2,3,4,6]  #array

no=int(input())       #input element

n=len(ex_array)       #length of array


if no<ex_array[0]:        #if element smaller then first element of array then add it to first position
    ex_array.insert(0,no)
elif no>ex_array[n-1]:    #else if element greater then last element of array then append it to array
    ex_array.append(no)
else:                     #else searching the right position of element in array
    for i in range(len(ex_array)-1,0,-1):
        if ex_array[i]<no:
            ex_array.insert(i+1,no)  #inserting element to it`s right postion
            break
            
print(ex_array)  #printing the updated array
