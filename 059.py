import string

contents = [int(i) for i in open("cipher1.txt").read().split(',')]

def apply(key):
  key = key * 400 + key[0]
  c = list(contents)
  for i in range(len(c)):
    c[i] = c[i] ^ ord(key[i])
  return ''.join(chr(x) for x in c)

keys = [k.strip() for k in open("3letters.txt")]

for k in keys:
  txt = apply(k)
  if 'the' in txt and 'to' in txt and 'and' in txt:
    print k, sum(ord(c) for c in txt)

