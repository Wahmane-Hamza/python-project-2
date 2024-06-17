def estpremier(a):
        if a>1:
            for i in range (2,a):
                if (a%i)==0 :
                    return False
                    break
            else:
                return True
                
def premier(a):
    while True:
        a=a+1
        if estpremier(a)==True:
            print(a)
            break
        
a=int(input('ecricre number :'))
if estpremier(a)==True:
    print('--> yes')
else:
    print('--> no')

premier(a)




