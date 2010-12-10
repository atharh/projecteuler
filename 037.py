primes = set([int(p.strip()) for p in open("primes.txt")])

def ist(n):
  s = str(n)
  for i in range(1, len(s)):
    if int(s[i:]) not in primes:  return False
    if int(s[:-i]) not in primes: return False
  return True

ts = []
for p in primes:
  if ist(p): ts.append(p)

print ts
print sum(ts) - 2 - 3 - 5 - 7 # 2, 3, 5 and 7 are not considered 
