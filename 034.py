factorials = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120,
              6: 720, 7: 5040, 8: 40320, 9: 362880}


def sum_digits_fact(n):
    sum = 0
    for d in str(n):
        sum += factorials[int(d)]
    return sum

def f(n):
    sum = 0
    for i in range(3, n):
        t = sum_digits_fact(i)
        if t == i:
            sum += i
    return sum

print f(100000)
