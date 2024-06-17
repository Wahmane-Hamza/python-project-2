import math
y=input('type the Equation like this (a*x^2+b*x+c): ')
list(y)
a=float(y[0])
b=float(y[6])
c=float(y[10])
delta= (b**2)-(4*a*c)
if delta>0:
    x1=int((-b+(math.sqrt(delta)))/2*a) 
    x2=int((-b-(math.sqrt(delta)))/2*a)
    print('we have delta=',delta,'so the Equation answer is X1=',x1,' and X2=',x2)
elif delta==0:
    x=int(-b/(2*a))
    print('we have delta=',delta,'so the Equation answer is X=',x)
else: 
    print('we have dealta=',delta,' so the Equation not have answer')