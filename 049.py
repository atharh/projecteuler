from primes import primes_less_than
from collections import defaultdict

table = defaultdict(list)

primes = primes_less_than(100000)
primes = [x for x in primes if len(str(x)) == 4]
#print primes

def key(p):
    return ''.join(sorted(str(p)))

def get_arith_seq(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            for k in range(j+1, len(seq)):
                #print seq[i], seq[j], seq[k]
                if seq[j]-seq[i] == seq[k]-seq[j]:
                    return (str(seq[i]), str(seq[j]), str(seq[k]))
    return None

for p in primes:
    table[key(p)].append(p)

for k in table.keys():
    if len(table[k]) > 3:
        seq = get_arith_seq(table[k])
        if seq is not None:
            print ''.join(seq)

        
