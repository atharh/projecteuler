import sys
import copy
from collections import defaultdict

li = [
  [131, 673, 234, 103, 18],
  [201, 96, 342, 965, 150],
  [630, 803, 746, 422, 111],
  [537, 699, 497, 121, 956],
  [805, 732, 524, 37, 331],
]

#li = [[int(l) for l in line.split(',')] for line in open("matrix.txt") ]

def get_graph(li):
  g = defaultdict(list)
  dim = len(li)
  for i in range(dim):
    for j in range(dim):
      x = li[i][j]
      if i != 0: g[x].append(li[i-1][j]) # move up
      if i < dim-1: g[x].append(li[i+1][j]) # move down 
      if j < dim-1: g[x].append(li[i][j+1]) # move right
  return g

def nmin(q, d):
  m = d[q[0]]
  r = q[0]
  for n in q:
    if d[n] < m:
      m = d[n]
      r = n
  return r

def dijkstra(g, src):
  d = defaultdict(lambda: 1e308)
  p = dict()
  for v in g:
    d[v] = 1e308
    p[v] = -1
  d[src] = 0
  q = g.keys()
  while len(q) != 0:
    u = nmin(q, d)
    q.remove(u)
    for v in g[u]:
      if not v in q: continue
      alt = d[u] + v
      if alt < d[v]:
        d[v] = alt
        p[v] = u
  return p
    
x = copy.deepcopy(li)

import pprint
pprint.pprint(x)

g = get_graph(li)
pprint.pprint(dijkstra(g, 131)) 
