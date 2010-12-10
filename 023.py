import sys

def get_proper_divisors(n):
    li = [1]
    for i in xrange(2, n/2+1):
      if n % i == 0: li.append(i)
    return li

def is_abundant(n):
    if sum(get_proper_divisors(n)) > n:
        return True
    return False


def all_abundants():
    ubound = 28124
    return [i for i in xrange(1, ubound) if is_abundant(i)]

abundants = all_abundants()

z = set()
for a in abundants:
    for b in abundants:
        c = a+b
        if c < 28124: z.add(c)

print sum(i for i in xrange(0, 28124) if i not in z)
