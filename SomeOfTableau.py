ask=int(input('type some of array :'))
T=[]
T2=[]
S=[]

print('Tableau 1 ')

for i in range(1,ask+1):
    print("array", i ,' = ', end=(''))
    a=int(input())
    T.append(a)


print('Tableau 2 ')

for i in range(1,ask+1):
    print("array", i ,' = ', end=(''))
    b=int(input())
    T2.append(b)


for i in range(0,len(T)):
    S.append(T[i]+T2[i])


print('TABLEAU 1 = ',T)
print('TABLEAU 2 = ',T2)
print('la some de 2 tableau',S)