n, b = [int (i) for i in input().split()]
cows = []

for i in range (n):
  p, s = [int (j) for j in input().split()]
  cows.append ([p // 2, s, p + s])

cows.sort (key = lambda x: x[2])

total = 0
counter = 0

for i in cows:
  if i[2] <= b - total:
    total += i[2]
    counter += 1
  elif i[0] + i[1] <= b - total:
    total += i[0] + i[1]
    counter += 1
    break

print (counter)
