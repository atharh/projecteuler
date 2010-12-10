from itertools import takewhile
from math import sqrt

primes = [int(p) for p in open("primes.txt")]
pset = set(primes)

corner = 1
side = 1
step = 2
pc = 0
dsize = 1

def isprime(p):
  if p < primes[-1]: 
    return p in pset
  else:
    lim = int(sqrt(p)) + 1
    for i in takewhile(lambda x: x<lim, primes):
      if p%i == 0: return False
    return True

counter = 0
while True:
  counter += 1
  for j in range(4):
    corner += step
    if isprime(corner): pc += 1
  dsize += 4 
  step += 2
  side += 2
  ratio = float(pc)/dsize * 100
  print pc, dsize, ratio, side
  if ratio < 10: 
    break

print side
