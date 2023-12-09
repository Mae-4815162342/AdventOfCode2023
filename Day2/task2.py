import re

def parse_game(line):
  """parses a game line into its power"""
  temp = line.split(":")
  game = int(re.sub("[^0-9]", "", temp[0]))

  temp = temp[1].replace("\n", "")
  subsets = temp.split(";")
  min_cubes = {"red":0, "blue":0, "green":0}

  for reavealed in subsets:
    values = reavealed.split(",")
    for val in values:
      temp = [v for v in val.split(" ") if v != '']
      number = int(temp[0])
      color = temp[1]
      if min_cubes[color] < number:
        min_cubes[color] = number
      
  return min_cubes["red"] * min_cubes["blue"] * min_cubes["green"]


def count_power_games(datas):
  sum = 0
  for line in datas:
    power = parse_game(line)
    sum += power
  return sum

# TEST
games = [
"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n"
]
assert(count_power_games(games) == 2286)

file = './Day2/games.txt'
with open(file) as f:
  games = f.readlines()

print(count_power_games(games))