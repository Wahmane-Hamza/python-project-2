def StarHalfTriangle(number):
    for i in range(0,number+1):
        star=''
        for i in range(i):
            star=star+'*'
        print(star)

#--------------------------------

def StarTriangle(number):
    for i in range(0,number+1):
        star=''
        space=''
        for j in range(i):
            star=star+' '+'*'

        for j in range(number-i):
            space=space+' '
        print(space,star)

#-------------------------------
def PascaleTriangle(number):
    p = [1]
    sss = number
    for i in range(number):
        pl = p + [1]
        for j in range(len(p)-1):
            pl[j+1] = p[j] + p[j+1]

        space = ''
        for a in range(sss, -1, -1):
            space += ' '

        pp = ''
        for r in range(0, len(p)):
            pp += str(p[r]) + ' '
        print(space, pp)
        sss -= 1
        p = pl
            

number=int(input('tayp the number : '))

StarHalfTriangle(number)
print('-------------------------------')
StarTriangle(number)
print('-------------------------------')
PascaleTriangle(number)
