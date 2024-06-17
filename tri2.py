def TriParInsertion(T):
    for i in range(0,len(T)):
        post=T[i]
        j   =i
        while j>0 and T[j-1]>post:
            r=T[j]
            T[j]=T[j-1]
            T[j-1]=r
            j=j-1
    return T

print(TriParInsertion([3,2,1]))