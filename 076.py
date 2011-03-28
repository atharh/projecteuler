from mine import memoize

def count_change(n):
    return cc(n, n-1)

@memoize
def cc(n, k):
    if n == 0:
        return 1
    elif n < 0 or k == 0:
        return 0
    return cc(n, k-1) + cc(n-fd(k), k)

def fd(k):
    return k

print count_change(5)
print count_change(100)
