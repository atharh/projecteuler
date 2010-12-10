from euler import gcd
from euler import erat
from mine import memoize
import mine
import sys
from collections import defaultdict
import itertools
import math

def sieve(limit):
  factors = defaultdict(list)
  for i in xrange(2, limit):
    if len(factors[i]) == 0:
      for j in xrange(i, limit, i):
        factors[j].append(i)
  return factors

factors = sieve(1001000)

@memoize
def totient(n):
  if n == 2: return 1
  num = n
  den = 1
  for pf in factors[n]:
    num *= pf-1
    den *= pf
  return num/den

max = -1.0
num = 0
for n in xrange(1, 1000001):
  c = float(n) / totient(n)
  if c > max:
    max = c
    num = n

print num
