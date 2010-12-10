import math

max = 0
lno = 0
for i, line in enumerate(open('base_exp.txt')):
  b, e = line.strip().split(',')
  x = int(e) * math.log10(int(b))
  if x > max: 
    max = x
    lno = i+1

print lno
