primes = [int(p.strip()) for p in open("primes.txt")]

def pfacts(n):
  facts = set()
  for p in primes:
    if n % p != 0: continue
    while n % p == 0:
      n = n / p
      facts.add(p)
    if n == 1: break
  return facts

for i in range(2, 134045):
  npf = len(pfacts(i))
  if npf != 4: continue
  if len(pfacts(i+1)) == 4 and len(pfacts(i+2)) == 4 and len(pfacts(i+3)) == 4:
    print i
