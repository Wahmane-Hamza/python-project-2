def insertion(T):
    for i in range(0,len(T)):
        var=T[i]
        j=i

        while j>0 and T[j-1]>var:
            r = T[j]
            T[j]=T[j-1]
            T[j-1] = r
            j=j-1

    return T
    
T=[]
a=int(input('Ecrire le nombre des element de tableau : '))
for i in range(1,a+1):
    print('Number ', str(i),' : ', end=(''))
    b=int(input())
    T.append(b)
print('votre Tableu --> ',T)
print('Le Tableau Ordonne -->',insertion(T))

