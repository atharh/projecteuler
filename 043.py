def ispand(n):
    s = ''.join(sorted(str(n)))
    return s == "0123456789"

def udiv(n):
    s = str(n)
    l = [2, 3, 5, 7, 11, 13, 17]
    
    for i, x in enumerate(l):
        #print i, x, s[i+1:i+4]
        if int(s[i+1:i+4]) % x != 0:
            return False
    return True

def nrd(n):
    s = str(n)
    return len(set(s)) == len(s)

def pans():
    tmp = []
    
    def r(tmp, n):
        tt = []
        for t in tmp:
            for y in (str(yy) for yy in range(n, 1000, n) if nrd(yy)):
                ss = '%03d' % int(y)
                if ss.startswith(t[-2:]):
                    tt.append(t + ss[-1])
        return [t for t in tt if nrd(t)]

    for i in range(1, 10):
        si = str(i)
        for y in (str(yy) for yy in range(100, 1000, 2) if nrd(yy) and si not in str(yy)):
            tmp.append(si+y)
    
    l = [3, 5, 7, 11, 13, 17]
    for e in l: 
        print 'doing ', e
        tmp = r(tmp, e)

    return tmp

tmp = pans()

sum = 0
for t in tmp:
    if nrd(t) and ispand(t):
        #print t
        sum += long(t)

print sum
