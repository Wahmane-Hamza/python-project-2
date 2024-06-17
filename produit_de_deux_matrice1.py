a = []
b = []
c = []

ligne = int(input("Nombre des ligne du matrice 1 :"))
colone1 = int(input("Nombre des colone du matrice 1 :"))
colone2 = int(input("Nombre des colone du matrice 2 :"))

print("----------------------------------------")
print("saisir les element de la matrice a: ")
for i in range(ligne) :
    t = []
    for j in range(colone1) :
        print("a[" ,i+1,"][",j+1,"]=",end=" ")
        t.append(int(input()))
    a.append(t)
print(a)
print("--------------------------------------------") 

print("saisir les element de la matrice b: ")
for i in range(colone1) :
    t = []
    for j in range(colone2) :
        print("b[" ,i+1,"][",j+1,"]=",end=" ")
        t.append(int(input()))
    b.append(t)
print(b)

for i in range(ligne) :      
    t=[]
    for j in range(colone2) :     
        t.append(0)
    c.append(t) 

for i in range(ligne):            
    for j in range(colone2):     
        S = 0
        for h in range(colone1): 
            c[i][j] = S + a[i][h] * b[h][j]
            S = c[i][j]

print("||--------------------------------------------------------------||")
print("||                                                              ||")
print("||  Le Produit des deux matrices est : ", c," ||")
print("||                                                              ||")
print("||--------------------------------------------------------------||")
