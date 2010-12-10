import itertools

def gcd(a, b):
  if b == 0: return a
  return gcd(b, a % b)

def divisors(n):
    li = [1]
    for i in xrange(2, n/2+1):
      if n % i == 0: li.append(i)
    return li

def is_rprime(x, y):
  xds = set(divisors(x))
  yds = set(divisors(y))
  return xds.difference(yds) == xds

def erat():
  d = {}
  yield 2
  for q in itertools.islice(itertools.count(3), 0, None, 2):
    p = d.pop(q, None)
    if p is None:
      d[q*q] = q
      yield q
    else:
      x = p + q
      while x in d or not (x&1):
        x += p
      d[x] = p
