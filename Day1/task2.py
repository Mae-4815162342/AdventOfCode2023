NUMBERS = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def find_value(text):
  """Finds first and last number (including written values) in text to form a two-digit number"""
  i = 0
  j = len(text)
  first_number = -1
  last_number = -1

  while i < len(text) or j >= 0:
    if first_number >= 0 and last_number >= 0:
      break
    if first_number == -1:
      first = text[i]
      if first.isdigit():
        first_number = int(first)
      else:
        for num in NUMBERS.keys():
          if text[i:i + len(num)] == num:
            first_number = NUMBERS[num]
      i += 1

    if last_number == -1:
      last = text[j - 1]
      if last.isdigit():
        last_number = int(last)
      else:
        for num in NUMBERS.keys():
          if text[j - len(num): j] == num:
            last_number = NUMBERS[num]
      j-=1

  return first_number * 10 + last_number

def compute_sum(lines):
  """Computes sum of values in a set of lines"""
  sum = 0
  for line in lines:
    sum += find_value(line)
  return sum

# TEST
lines = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
assert(compute_sum(lines) == 281)

# with values
file = './Day1/calibration.txt'

with open(file) as f:
  lines = f.readlines()

sum = compute_sum(lines)
print(sum)