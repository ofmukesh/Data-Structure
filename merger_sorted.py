num1=[1,2,4,5]
num2=[3,6]
merged=[]
length=len(num1)+len(num2)

for i in range(length):
    if len(num1)==0:
        merged.append(num2[0])
        num2.pop(0)
    elif len(num2)==0:
        merged.append(num1[0])
        num1.pop(0)
    elif num1[0]<=num2[0]:
        merged.append(num1[0])
        num1.pop(0)
    elif num2[0]<num1[0]:
        merged.append(num2[0])
        num2.pop(0)
print(merged)
