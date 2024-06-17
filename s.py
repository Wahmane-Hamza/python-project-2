num=int(input('! '))
stri=''
s=1
i=num
if num==0:
    print('0! = 1')
else:
    while i>0:
        if i==1:
            stri=stri+str(i)+'='
        else:
            stri=stri+str(i)+'*'
        s=s*i
        i=i-1
stri=stri+str(s)
print(stri)        
