n = int (input())
hay_bales = [int (input()) for i in range (n)]

average = 0
for i in hay_bales:
  average += i
average //= n

moves = 0
for i in hay_bales:
  if i > average:
    moves += (i - average)

print (moves)
