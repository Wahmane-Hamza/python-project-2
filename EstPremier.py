def estpremier(a):
            for i in range (2,a):
                if (a%i)==0 :
                    return False
                    break
            else:
                return True
        



def ExtraireMarsPrenier(a):
    for i in range(2,a):
        if estpremier(i)==True:
            print(i)

def ExtraireMarsPrenier2(x):
    j=0
    b=a-1
    for i in range(2,x):
        while True :
            if estpremier(i)==True:
                return j
            if x==b:
                break 
            j=j+1
    print(i)

a=int(input('ecricre number :'))
if estpremier(a)==True:
    print('--> yes')
else:
    print('--> no')


    





