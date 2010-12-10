def ispand19(n):
  s = ''.join(sorted(list(str(n))))
  return s == "123456789"

seen = set()
sum = 0
for i in xrange(1, 10000):
  if i < 100:
    x = 999
  elif i < 1000:
    x = 99
  else:
    x = 9
  for j in xrange(1, x):
    q = str(i) + str(j) + str(i*j)
    if len(q) > 9: continue
    if i*j in seen: continue
    if ispand19(q):
      seen.add(i*j)
      sum += i * j

print sum
