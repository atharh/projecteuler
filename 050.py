primes = [int(p.strip()) for p in open("primes.txt")]
setp = set(primes)

d = {}

def chain_sum(n):
  sum = 0
  for i in range(n):
    sum += primes[i]
  return sum

def doit():
  max = -1
  prime = -1
  for p in primes:
    if p > 1e3: break
    cl = chain_length(p)
    if cl > max: 
      max = cl
      prime = p
  print prime, max

print chain_sum(23)
