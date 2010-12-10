def bouncy(n):
  s = str(n)
  rs = str(n)[::-1]
  if s == ''.join(sorted(s)) or rs == ''.join(sorted(rs)):
    return False
  return True


def find():
  count = 0
  for i in range(1, 10000000):
    if bouncy(i): count += 1.0
    x = count / i * 100
    print i, x
    if x >= 99: return i
  return -1

print find()
