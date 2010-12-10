from itertools import count

c = 0
seen = set()
for i in xrange(1, 1000):
  for j in xrange(1, 100):
    if len(str(i**j)) < j: break
    if len(str(i**j)) == j:
      if i**j not in seen: c += 1
      seen.add(i**j)

print c
