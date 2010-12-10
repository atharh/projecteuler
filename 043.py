"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting 
sub-string divisibility property.

Let d_(1) be the 1^(st) digit, d_(2) be the 2^(nd) digit, and so on. In this 
way, we note the following:

* d_(2)d_(3)d_(4)=406 is divisible by 2
* d_(3)d_(4)d_(5)=063 is divisible by 3
* d_(4)d_(5)d_(6)=635 is divisible by 5
* d_(5)d_(6)d_(7)=357 is divisible by 7
* d_(6)d_(7)d_(8)=572 is divisible by 11
* d_(7)d_(8)d_(9)=728 is divisible by 13
* d_(8)d_(9)d_(10)=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

def perm(l):
    if len(l) <= 1:
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i+1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i+1] + x)
    return r

print perm(range(10))

def ispand09(n):
  s = ''.join(sorted(list(str(n))))
  return s == "0123456789"

def udiv(n):
  s = str(n)
  r = True
  l = [2, 3, 5, 7, 11, 13, 17]
  for k, i in enumerate(xrange(1, 8)):
    r = r and (int(s[i:i+3]) % l[k] == 0)
  return r

print udiv(1406357289)
