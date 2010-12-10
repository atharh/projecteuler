"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

^(1)/_(2) =   0.5
^(1)/_(3) =   0.(3)
^(1)/_(4) =   0.25
^(1)/_(5) =   0.2
^(1)/_(6) =   0.1(6)
^(1)/_(7) =   0.(142857)
^(1)/_(8) =   0.125
^(1)/_(9) =   0.(1)
^(1)/_(10)  =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that ^(1)/_(7) has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^(1)/_(d) contains the longest recurring cycle in its decimal fraction part.
"""
def getl(n):
  d = set()
  x = 1
  cycle = []
  while 1:
    x, r = divmod(x*10, n)
    if x in d: break
    cycle.append(str(x)) 
    d.add(x)
    x = r
  return ''.join(cycle)


print getl(997)