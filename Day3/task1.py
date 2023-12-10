import numpy as np

def parse_schematics(schematics):
  """From a list of lines from an engine schematics, produces a table of influence zone for symbols
  and a list of each number's positions"""
  len_line = len(schematics[0])
  len_schem = len(schematics)
  influence_zone = np.zeros((len_schem, len_line))
  numbers_positions = {}
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
        if char != '.' and char != '\n':

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

          for k in available_i_index:
            for l in available_j_index:
              influence_zone[k,l] = 1
          
        if len(current_positions) > 0:
          if current_number not in numbers_positions:
            numbers_positions[current_number] = [current_positions]
          else:
            numbers_positions[current_number] += [current_positions]
          current_number = 0
          current_positions = []
  return numbers_positions, influence_zone

def count_adjacent_to_symbol(schematics):
  """Counts the sum of parts adjencent to a symbol in shematics"""
  numbers_positions, influence_zone = parse_schematics(schematics)
  sum = 0
  for num in numbers_positions.keys():
    positions_list = numbers_positions[num]
    for positions in positions_list:
      for i,j in positions:
        if influence_zone[i,j] == 1.0:
          sum += num
          break
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
assert(count_adjacent_to_symbol(schematics) == 4361)

file = './Day3/engine_schematic.txt'
with open(file) as f:
  schematics = f.readlines()
print(count_adjacent_to_symbol(schematics))
