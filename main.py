from random import randint
choices = ['ROCK', 'PAPER', 'SCISSORS', "SPOCK", 'LIZARD', 'STOP']
player_input = input('-> ROCK, PAPER, SCISSORS, LIZARD, OR SPOCK? ')
cpu = randint(1,5)
if player_input != "stop":
  for i in range(6):
    if str(player_input).upper() == choices[i - 1]:
      player_one = i
      i = 7
  if(cpu == player_one):
    print('You Tied')
  elif(cpu + 1 == player_one)or(cpu + 3 == player_one)or(player_one + 4 == cpu)or(player_one + 2 == cpu):
    print('You won!')
  else:
    print('You lost!')