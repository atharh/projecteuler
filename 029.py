import math

s = set()
for a in xrange(2, 101):
    for b in xrange(2, 101):
        s.add(math.pow(a, b))

print len(s)
