from itertools import count

def ftn():
  c = count(286)
  while 1:
    n = c.next()
    yield n * (n+1) / 2

def fpn():
  c = count(166)
  while 1:
    n = c.next()
    yield n * (3*n - 1) / 2

def fhn():
  c = count(144)
  while 1:
    n = c.next()
    yield n * (2*n - 1)

tn = ftn()
pn = fpn()
hn = fhn()
t = tn.next()
p = pn.next()
h = hn.next()

while 1:
  m = max([t, p, h])
  while t < m: t = tn.next()
  while p < m: p = pn.next()
  while h < m: h = hn.next()

  if t == p and t == h:
    print t
    break
