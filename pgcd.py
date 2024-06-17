def pgcd(a):
        if a>1:
            for i in range (2,a):
                if (a%i)==0 :
                    return False
                    break
            else:
                return True
        
a=int(input('ecricre number :'))
if pgcd(a)==True:
    print('--> yes')
else:
    print('--> no')


    





