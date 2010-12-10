def cf(a, b):
  al = list(str(a))
  bl = list(str(b))
  lal = len(al)
  lbl = len(bl)

  for x in al:
    if x in bl:
      al.remove(x)
      bl.remove(x)
    
  if len(al) == lal: return False
  n, d = int(''.join(al)), int(''.join(bl))
  if d == 0: return False
  return float(a)/b == float(n)/d

num = 1
den = 1
for i in range(10, 100):
  for j in range(10, 100):
    if i == j: continue
    if sorted(str(i)) == sorted(str(j)): continue
    if cf(i, j) and float(i)/j < 1 and i % 10 != 0:
      print i, j
      num *= i
      den *= j

print num, den
