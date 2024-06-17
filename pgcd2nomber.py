def pgcd(a,b):
    if a>b:
        c=a
        a=b
        b=c
        if a>1:
            for i in range (2,a):
                if (a%i)==0 and (b%i)==0:
                    return False
                    break
                elif (a%i)==0 and not((b%i)==0):
                    return False
                    break
                elif not((a%i)==0) and (b%i)==0:
                    return False
                    break
            else:
                return True
        
a=int(input('ecricre number :'))
b=int(input('ecricre number 2:'))
if pgcd(a,b)==True:
    print()
    print('----->yes')
else:
    print()
    print('----->NO')

    


       
    
             