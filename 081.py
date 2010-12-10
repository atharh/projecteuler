import sys
import copy

li = [
  [131, 673, 234, 103, 18],
  [201, 96, 342, 965, 150],
  [630, 803, 746, 422, 111],
  [537, 699, 497, 121, 956],
  [805, 732, 524, 37, 331],
]

li = [[int(l) for l in line.split(',')] for line in open("matrix.txt") ]

x = copy.deepcopy(li)

for i in range(len(li)):
  for j in range(len(li)):
    if i == 0 and j == 0: continue
    elif i == 0: x[i][j] += x[i][j-1]
    elif j == 0: x[i][j] += x[i-1][j]
    else: x[i][j] += min(x[i-1][j], x[i][j-1])

i = len(li)-1
j = len(li)-1
sum = 0
while 1:
  print i, j
  sum += li[i][j]
  if i == 0 and j == 0: break
  if x[i-1][j] < x[i][j-1]:
    i -= 1
  else:
    j -= 1

print sum
