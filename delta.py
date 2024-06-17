import math
print('a*x^2+b*x+c')
Numbera = int(input('type a: '))
Numberb = int(input('type b: '))
Numberc = int(input('type c: '))
delta =(Numberb**2)-(4*Numbera*Numberc)

if delta>0:
    x1=int((-Numberb+(math.sqrt(delta)))/2*Numbera) 
    x2=int((-Numberb-(math.sqrt(delta)))/2*Numbera) 
    print('we have delta=',delta,'so the Equation answer is X1=',x1,' and X2=',x2)
elif delta==0:
    x=int(-Numberb/(2*Numbera))
    print('we have delta=',delta,'so the Equation answer is X=',x)
else: 
    print('we have dealta=',delta,' so the Equation not have answer')
