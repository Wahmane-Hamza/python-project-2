deja=input('Est ce que vous déjà une assurance avec nous? oui/non : ')

if (deja=='oui'):
    color=input('Quel est le couleur de votre assurance: ')
    ksida=int(input('Combien daccidents que vous avez déjà fait?: '))
    
    if color=='rouge' and ksida==0:
        print('le couleur de votre assurance est orange')
    
    elif color=='orange' and ksida==0:
        print('le couleur de votre assurance est vert')
    
    elif color=='vert' and ksida==0:
        print('le couleur de votre assurance est blue') 
    
    elif color=='blue':
        if ksida==0:
            print('le couleur de votre assurance est blue')
        elif ksida==1:
            print('le couleur de votre assurance est vert')
        elif ksida==2:
            print('le couleur de votre assurance est orange')
        else:
             print('votre assurance est refusé')
    
    else:
        print('Votre demande est refusétu va resté dans ce couleur')


elif (deja=='non'):
    age= int(input('Quel est vôtre âge?: '))
    
    
    if age<25:
        pirmi= int(input('Combien dannées que vous avez prendre votre permis: '))
        if pirmi>=2:
           print('le couleur de votre assurance est orange')
        elif pirmi<2:
            ksida=int(input('Combien daccidents que vous avez déjà fait?: '))
            if ksida==0:
                print('le couleur de votre assurance est rouge')
            else:  
                print('votre assurance est refusé')
    
    
    elif age>=25:
       pirmi= int(input('Combien dannées que vous avez prendre votre permis: '))
       
       if pirmi<2:
          ksida=int(input('Combien daccidents que vous avez déjà fait?: '))
          if ksida==0:
            print('le couleur de votre assurance est orange')   
          else:
            print('votre assurance est refusé')  
       
       elif pirmi>=2 :
          ksida=int(input('Combien daccidents que vous avez déjà fait?: '))
          if ksida==0:
            print('le couleur de votre assurance est vert')
          elif ksida==1:
            print('le couleur de votre assurance est orange')
          elif ksida==2:
            print('le couleur de votre assurance est rouge') 
          else:  
            print('votre assurance est refusé') 



            


