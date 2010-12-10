def dss(n):
  s = str(n)
  sum = 0
  for x in s: sum += int(x)**2
  return sum

def arrives(n):
  x = n
  while 1:
    x = dss(x)
    if x == 1 or x == 89: break
  return x == 89

d = set()
count = 0
for i in range(1, 10000000):
  if dss(i) in d:
    count += 1
    continue
  if arrives(i):
    d.add(dss(i))
    count += 1

print count
