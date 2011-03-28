import sys
import copy
from collections import defaultdict

li = [
  [131, 673, 234, 103, 18],
  [201, 96, 342, 965, 150],
  [630, 803, 746, 422, 111],
  [537, 699, 497, 121, 956],
  [805, 732, 524, 37, 331],
]

#li = [[int(l) for l in line.split(',')] for line in open("txt/matrix.txt") ]

dim = len(li)

cost = [0] * dim

for i in range(dim):
    print range(dim)
    for j in range(dim):
        cost[j] = min(cost[j], cost[j-1]) + li[j][i]
        print i, j, cost
    print list(reversed(range(dim-2)))
    for j in reversed(range(dim-2)):
        cost[j] = min(cost[j], cost[j+1] + li[j][i])
        print i, j, cost
    raw_input()

print cost
print min(cost)


def f():
    for i in range(dim):
        #print li[i][dim-1]
        j = dim-1
        k = i
        sum = 0
        while j >= 0:
            print k, j
            if j == 0:
                sum += li[k][0]
                j -= 1
            elif j == dim-1:
                sum += li[k][j-1]
                j -= 1
            elif k == 0:
                m = min(li[k][j-1], li[k+1][j])
                sum += m
                if m == li[k+1][j]:
                    k += 1
                else:
                    j -= 1
            elif k == dim-1:
                m = min(li[k][j-1], li[k-1][j])
                sum += m
                if m == li[k][j-1]:
                    j -= 1
                else:
                    k -= 1
            else:
                m = min(li[k][j-1], li[k-1][j], li[k+1][j])
                sum += m
                if m == li[k][j-1]:
                    j -= 1
                elif m == li[k-1][j]:
                    k -= 1
                else:
                    k += 1

            raw_input()
        print sum
        li[i][dim-1] = sum

    print li


