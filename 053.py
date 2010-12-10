factorials = {}

def fact(n):
  if n == 0: return 1
  return reduce(lambda x, y: x*y, range(1, n+1))

def ncr(n, r):
  return factorials[n] / (factorials[r] * factorials[n-r])

# generate all factorials
for i in range(0, 101):
  factorials[i] = fact(i)


count = 0

for i in range(23, 101):
  for j in range(0, i+1):
    if ncr(i, j) > 1000000: count += 1

print count
