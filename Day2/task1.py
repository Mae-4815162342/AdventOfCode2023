import re

CUBES = {"red":12, "green": 13, "blue": 14}

def parse_game(line):
  """parses a line into its number or 0 if the count is not possible"""
  temp = line.split(":")
  game = int(re.sub("[^0-9]", "", temp[0]))

  temp = temp[1].replace("\n", "")
  subsets = temp.split(";")
  for reavealed in subsets:
    values = reavealed.split(",")
    for val in values:
      temp = [v for v in val.split(" ") if v != '']
      number = int(temp[0])
      color = temp[1]
      if color not in CUBES:
        return 0
      elif CUBES[color] < number:
        return 0
      
  return game


def count_possible_games(datas):
  sum = 0
  for line in datas:
    game = parse_game(line)
    sum += game
  return sum

# TEST
games = [
"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n"
]
assert(count_possible_games(games) == 8)

file = './Day2/games.txt'
with open(file) as f:
  games = f.readlines()

print(count_possible_games(games))