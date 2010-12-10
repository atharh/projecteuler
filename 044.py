def penta(n):
  return n * (3*n - 1) / 2

pentas = []

for i in range(1, 10000):
  pentas.append(penta(i))

sp = set(pentas)

min = 1e308

print "starting"

for p in pentas:
  for q in pentas:
    if p+q in sp and abs(p-q) in sp:
      print p, q
      if abs(p-q) < min: min = abs(p-q)

print min
