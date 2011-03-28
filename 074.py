from mine import memoize

@memoize
def fact(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

@memoize
def factsum(n):
    return sum(fact(int(i)) for i in str(n))


g = {}
@memoize
def chain(n):
    x = n
    count = 1
    seen = set()
    seen.add(n)
    while 1:
        x = factsum(x)
        #print x, 
        if x in seen:
            break
        if g.has_key(x):
            g[n] = count + g[x]
            return g[n]
        else:
            seen.add(x)
            count += 1
    g[n] = count
    return count


def f():
    count = 0
    for i in range(1000000):
        #print i
        if chain(i) == 60:
            count += 1
    print count

f()
