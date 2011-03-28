from primes import primes_less_than

primes = set(primes_less_than(1000000))
print 'starting ..'
def iss(p):
    count = 0
    #seen = set()
    li = list(str(p))
    for x in range(10):
        for i in range(len(li)):
            for j in range(len(li)):
                ii = li[i]
                jj = li[j]
                li[i] = li[j] = str(x)
                #print int(''.join(li))
                y = int(''.join(li))
                #print y
                #if x in seen: continue
                if y in primes:
                    #seen.add(x)
                    #print li
                    count += 1
                li[i] = ii
                li[j] = jj
    if count == 8:
        return True
    return False

for p in primes:
    if iss(p):
        print p
