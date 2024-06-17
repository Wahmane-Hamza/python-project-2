T=[]
T2=[]
ST=[]
print('▓▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▓')
irtifa3= int(input('▓ numbre de ligne de premier  matrice :▓-->'))
l3ard= int(input('▓ numbre de colon de premiere matrice :▓-->'))
l3ard2=int(input('▓ numbre de colon de deuxieme matrice :▓-->'))
print('▓▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▓')


print('֍-------------------֍')
print('| TABLEAU NUMBER 1  |')
print('֍-------------------֍')
print('____________________________')
for i in range(1,irtifa3+1):
    a=[]
    for j in range(1,l3ard+1):
        print('ligne [',str(i),'] on colone [',str(j),'] = ',end=(''))
        a.append(int(input('')))
    print()
    print('____________________________')
    T.append(a)

print('֍-------------------֍')
print('| TABLEAU NUMBER 2  |')
print('֍-------------------֍')
print('____________________________')
for i in range(1,l3ard+1):
    b=[]
    for j in range(1,l3ard2+1):
        print('ligne[',str(i),'] on colone[',str(j),'] =',end=(''))
        b.append(int(input('')))
    print('____________________________')
    print('')
    T2.append(b)


for i in range(irtifa3):
    c=[]
    for j in range(l3ard2):
        c.append(0)
    ST.append(c)



for i in range(len(T)):
    for j in range(len(T2[0])):
        some=0
        for k in range(len(T2)):
            some=some+ T[i][k]*T2[k][j]
            ST[i][j]=some
    
print('֍------PREMIER TABLEAU------֍')
print('|                           |')
print('|',T)
print('|                           |')
print('֍---------------------------֍')
print()
print('֍------DEUXIEME TABLEAU-----֍')
print('|                           |')
print('|',T2)  
print('|                           |')
print('֍---------------------------֍')
print()
print()
print('                              ֍------LE PRODUIT DES DEUX TALBLEAU------֍')
print('                              |                                        |')
print('                              |',ST)  
print('                              |                                        |')
print('                              ֍----------------------------------------֍')
