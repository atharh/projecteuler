import itertools
primes = set(int(p.strip()) for p in open("primes.txt"))

def getf(a, b):
  return lambda n: n**2 + a*n + b

def how_many(a, b):
  f = getf(a, b)
  count = 0
  for i in itertools.count(0):
    if f(i) not in primes: break
    count += 1
  return count

a = 0
b = 0
max = 0

for i in xrange(-999, 1000):
  for j in xrange(-999, 1000):
    hm = how_many(i, j)
    if hm > max:
      a, b, max = i, j, hm

print a, b, max, a*b
