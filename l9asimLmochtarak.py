a=int(input('type your first number : '))
b=int(input('type your secund number : '))

arr=[]
arr2=[]
arr3=[]
for i in range(1,a+1):
    if a%i==0:
        arr.append(i)
for i in range(1,b+1):
    if b%i==0:
        arr2.append(i)
for j in range(len(arr)):
    for f in range(len(arr2)):
        if arr[j]==arr2[f]:
            arr3.append(arr[j])
print(arr)
print(arr2)
print(arr3)

