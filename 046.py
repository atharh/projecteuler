from primes import primes_less_than
import math

primes = primes_less_than(10000)


def can(odd_number):
    for p in primes:
        if p > odd_number:
            break
        diff = odd_number - p
        if diff % 2 != 0:
            continue
        square = diff / 2
        x = int(math.sqrt(square))
        if x*x == square:
            return True
    return False

for i in range(35, 99999, 2):
    if not can(i): 
        print i
        break
