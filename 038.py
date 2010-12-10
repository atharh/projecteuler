from itertools import count

def ispand19(n):
  s = ''.join(sorted(list(str(n))))
  return s == "123456789"

def cprod(n):
  s = str(n)
  r = ''
  for x in count(1):
    r += str(n*int(x))
    if ispand19(r): return r
    if len(r) > 9: break
  return None

max = 0
for i in xrange(10000):
  cp = cprod(i)
  if cp is not None:
    if int(cp) > max: max = int(cp)

print max
