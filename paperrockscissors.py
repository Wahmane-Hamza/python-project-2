player1 = input('(paper / rock / scissors)' )
player2 = input('(paper / rock / scissors)' )
if player1==player2:
    print('draw!')
if player1=='rock' and player2=='scissors':
    print('player1 won!')
elif player1=='scissors' and player2=='paper':
    print('player1 won!')
elif player1=='paper' and player2=='rock':
    print('player1 won!')
elif not(player1==player2):
     print('player2 won!')

