base2_wrong = input()
base3_wrong = input()

def convert_base2 (n):
  binary = bin(n)[2:]
  return binary 

def convert_base3 (n):
  if n == 0:
    return '0'
  elif n < 0:
    return '-' + convert_base3(-n)
  else:
    digits = []
    while n != 0:
      n, remainder = divmod(n, 3)
      digits.append(str(remainder))
    return ''.join(digits[::-1])

def off_by_one_digit (n, real):
  n_list = list (str (n))
  real_list = list (str (real))
  count = 0
  if len(n_list) != len(real_list):
    return False
  for i in range (len (n_list)):
    if n_list[i] != real_list[i]:
      count += 1
  return count == 1

for i in range (1, 1000000001):
  base2 = convert_base2 (i)
  base3 = convert_base3 (i)
  if off_by_one_digit (base2_wrong, base2) and off_by_one_digit (base3_wrong, base3):
    print (i)
    break
