s=int(input('type some of array :'))
T=[]
T2=[]

for i in range(0,s):
    print("number", i , '=', end=(''))
    a=input()
    T.append(a)

for i in range(len(T)-1,-1,-1):
    T2.append(T[i])


print(T)
print(T2)