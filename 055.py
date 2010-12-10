def isp(n):
  return str(n) == str(n)[::-1]

def isl(n):
  sum = n
  for i in range(50):
    sum = sum + int(str(sum)[::-1])
    if isp(sum): return False
  return True

count = 0
for i in range(10000):
  if isl(i):
    count += 1

print count
