def fadd(a, b):
  return (a[0]*b[1] + a[1]*b[0]), a[1]*b[1]

def expand(n):
  sum = (1, 2)
  while n != 1:
    x = fadd((2, 1), sum)
    sum = (x[1], x[0])
    n -= 1
  return fadd((1, 1), sum)

count = 0
for i in range(1, 1001):
  n, d = expand(i)
  if len(str(n)) > len(str(d)): count += 1

print count
