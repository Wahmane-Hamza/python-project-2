x = float(input('ecrire le premier nombre:'))
z = input('selectionnez l operation que te veux:')
y = float(input('ecrire le deuxieme nombre:'))

if z == '+':
   s=x+y
   print('la Reponse est:',s)
elif z == '-':   
   s=x-y
   print('la Reponse est:',s)
elif z == '*':
    s=x*y
    print('la Reponse est:',s)
elif z == '/':
    s=x/y
    print('la Reponse est:',s)
elif z== 'dev':
    s=x//y
    print('la Reponse est:',s)
elif z== 'mod':
    s=x%y
    print('la Reponse est:',s)
    
else: error