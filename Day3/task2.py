import numpy as np

def parse_schematics(schematics):
  """From a list of lines from an engine schematics, produces a table of the numbers indexed in number_index
    and a list of each gears's influence position"""
  len_line = len(schematics[0])
  len_schem = len(schematics)
  numbers_positions = np.zeros((len_schem, len_line))
  id_gears = 1
  id_numbers = 1
  numbers_index = {}
  gears_positions = {}
  for i in range(len_schem):
    line = schematics[i]
    current_number = 0
    current_positions = []
    for j in range(len(line)):
      char = line[j]
      if char.isdigit():
        current_number = current_number * 10 + int(char)
        current_positions += [(i,j)]
      else:
        if char == '*':

          available_i_index = [i]
          if i - 1 >= 0:
            available_i_index += [i - 1]
          if i + 1 < len_schem:
            available_i_index += [i + 1]

          available_j_index = [j]
          if j - 1 >= 0:
            available_j_index += [j - 1]
          if j + 1 < len(line):
            available_j_index += [j + 1]

          gears_positions[id_gears] = [(k,l) for l in available_j_index for k in available_i_index ]
          id_gears += 1
          
        if len(current_positions) > 0:
          numbers_index[id_numbers] = current_number
          for k,l in current_positions:
            numbers_positions[k,l] = id_numbers
          current_number = 0
          current_positions = []
          id_numbers += 1
  return numbers_index, numbers_positions, gears_positions

def count_gear_ratio(schematics):
  """Counts the sum of gear ratio in shematics"""
  numbers_index, numbers_positions, gears_positions = parse_schematics(schematics)
  sum = 0
  for gear in gears_positions.keys():
    gear_numbers = set()
    for i,j in gears_positions[gear]:
      if numbers_positions[i,j] > 0:
        gear_numbers.add(numbers_positions[i,j])
    if len(gear_numbers) == 2:
      ratio = 1
      for number in gear_numbers:
        ratio *= numbers_index[number]
      sum += ratio
  return sum

# TEST
schematics = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split("\n")
assert(count_gear_ratio(schematics) == 467835)

file = './Day3/engine_schematic.txt'
with open(file) as f:
  schematics = f.readlines()
print(count_gear_ratio(schematics))
