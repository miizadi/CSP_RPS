from random import randint
choices = ['ROCK', 'PAPER', 'SCISSORS', "SPOCK", 'LIZARD', 'STOP']
player_input = input('-> ROCK, PAPER, SCISSORS, LIZARD, OR SPOCK? ')
while str(player_input).upper() != "STOP":
  cpu = randint(1,5)
  while not str(player_input).upper() in choices:
      print("ENTER A VALID OPTION")
      player_input = input('-> ROCK, PAPER, SCISSORS, LIZARD, OR SPOCK? ')
  if player_input != "stop":
    for i in range(6):
      if str(player_input).upper() == choices[i - 1]:
        player_one = i
        i = 7
    if(cpu == player_one):
        print('You Tied')
    elif(cpu + 1 == player_one)or(cpu + 3 == player_one)or(player_one + 4 == cpu)or(player_one + 2 == cpu):
        print(f'You used {choices[player_one - 1]} against {choices[cpu - 1]} and won!')
    else:
        print(f'You used {choices[player_one - 1]} against {choices[cpu - 1]} and lost!')
    player_input = input('-> ROCK, PAPER, SCISSORS, LIZARD, OR SPOCK? ')
print("Thanks for playing")