import re

def find_value(text):
  """Finds first and last number in text to form a two-digit number"""
  digits = re.sub("[^0-9]", "", text)
  return 10*int(digits[0]) + int(digits[-1])

def compute_sum(lines):
  """Computes sum of values in a set of lines"""
  sum = 0
  for line in lines:
    sum += find_value(line)
  return sum

# TEST
lines = ["1abc2\n", "pqr3stu8vwx\n", "a1b2c3d4e5f\n", "treb7uchet\n"]
assert(compute_sum(lines) == 142)

# with values
file = './Day1/calibration.txt'

with open(file) as f:
  lines = f.readlines()

sum = compute_sum(lines)
print(sum)