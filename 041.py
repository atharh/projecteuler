primes = (int(p.strip()) for p in open("primes.txt"))

def ispand(n):
  s = ''.join(sorted(list(str(n))))
  ns = ''.join(str(x) for x in range(1, len(s)+1))
  return s == ns

for p in primes:
  if ispand(p): print p

# last printed line is the solution
