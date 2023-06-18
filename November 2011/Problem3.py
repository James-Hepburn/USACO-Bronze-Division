n = int(input())
fj_notes = [int(input()) for i in range(n)]
c = int(input())
c_notes = sorted ([int(input()) for i in range(c)])

c_differences = [c_notes[i] - c_notes[i - 1] for i in range(1, c)]
indexes = []

for i in range(n - c + 1):
  sequence = sorted (fj_notes[i:i+c])
  sequence_differences = [sequence[j] - sequence[j - 1] for j in range(1, c)]
  if sequence_differences == c_differences:
    indexes.append(i + 1)

print(len(indexes))
for i in indexes:
  print(i)
