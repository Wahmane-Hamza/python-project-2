number=int(input('! '))
s=1
stri=''
i=number
if number==0:
    print('0! = 1')
else:
    while True:
        if (i==0):
            break
        else:
            if i==1 :
                stri=stri+str(i)+'='
            else:
                stri=stri+str(i)+'*'
            s=s*i
            i=i-1
    stri=stri+str(s)
    print(stri)