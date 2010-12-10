from euler import gcd
from euler import erat
from mine import memoize
import mine
import sys
from collections import defaultdict
import itertools
import math

@mine.timer
def sieve(limit):
  factors = defaultdict(list)
  for i in xrange(2, limit):
    if len(factors[i]) == 0:
      for j in xrange(i, limit, i):
        factors[j].append(i)
  return factors


primes = [int(p.strip()) for p in open('primes5m.txt')]

@memoize
def totient(n):
  if n == 2: return 1
  num = n
  den = 1
  pf = 1
  c = itertools.ifilter(lambda p: n % p == 0, primes)
  while 1:
    try:
      pf = c.next()
      num *= pf-1
      den *= pf
    except StopIteration:
      break
  return num/den

def lchain(n):
  c = 1
  x = n
  while x != 1:
    x = totient(x)
    c += 1
  return c

def doit():
  sum = 0
  for p in primes[::-1]:
    lc = lchain(p)
    print p, lc
    if lc == 25:
      print p
      sum += p
  return sum

print doit()
