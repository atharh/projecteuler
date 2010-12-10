import itertools
import re
import sys

r = re.compile('1\d2\d3\d4\d5\d6\d7\d8\d9\d0')

for i in xrange(1389026623, 0, -1):  
  print i
  if r.match(str(i*i)) is not None:
    print i
    break
