def count_match_in_card(card):
  """Counts matches in a single card line"""
  values = [ val for val in card.replace('\n', '').split(' ')[2:] if val !='']
  index_of_separation = values.index("|")
  ticket_numbers = values[:index_of_separation]
  values = values[index_of_separation + 1:]
  count = 0
  for val in values:
    if val in ticket_numbers:
      count +=1
  return count

def count_copies(cards):
  """Counts the number of scratchcards generated with the rule"""
  sum = 0
  cards_number = {i + 1:1 for i in range(len(cards))}
  for i in range(len(cards)):
    card = cards[i]
    copies = cards_number[i + 1] if i + 1 in cards_number else 1
    sum += copies
    points = count_match_in_card(card)
    for k in range(points):
      num = i + k + 2
      if num in cards_number:
        cards_number[num] += 1 * copies
  return sum

# TEST
cards="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')

assert(count_copies(cards)==30)

with open('cards.txt') as file:
  cards = file.readlines()
print(count_copies(cards))