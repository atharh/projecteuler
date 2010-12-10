from collections import defaultdict
from operator import itemgetter
import math

d = defaultdict(int)

seen = set()

for i in range(1001):
  for j in range(1001):
    k = math.sqrt(i**2 + j**2)
    p = i + j + k
    if p < 1000: d[p] += 1

print sorted(d.iteritems(), key=itemgetter(1), reverse=True)[:1]
