def get_digits (w):
  digits = []
  for i in str (w):
    digits.append (int (i))
  return digits

def check_carry (d1, d2):
  min_len = min (len (d1), len (d2))
  index1 = len (d1) - 1
  index2 = len (d2) - 1
  for i in range (min_len):
    if d1[index1] + d2[index2] > 9:
      return False
    index1 -= 1
    index2 -= 1
  return True

n = int (input ())
weights = []

for i in range (n):
  weights.append (int (input()))

answers = []

for i in range (n):
  total = weights[i]
  counter = 1
  for j in range (i + 1, n):
    digits1 = get_digits (total)
    digits2 = get_digits (weights[j])
    if check_carry (digits1, digits2) == True:
      counter += 1
      total += weights[j]
  answers.append (counter)

print (max (answers))
