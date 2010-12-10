d = {
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
  100: 'onehundred',
  1000: 'onethousand',
}

def to_words(n):
  w = []
  s = str(n)
  if n in d:
    w.append(d[n])
  elif n < 100:
    w.append(d[n - n%10])
    w.append(d[n % 10])
  elif n % 100 == 0:
    w.append(d[n/100])
    w.append('hundred')
  elif n > 100:
    w.append(d[n/100])
    w.append('hundred')
    w.append('and')
    n = n % 100
    if n in d: w.append(d[n])
    else:
      w.append(d[n - n % 10])
      if n % 10 != 0:
        w.append(d[n % 10])
  return ''.join(w)

li = []
for i in range(1, 1001):
  x = to_words(i)
  li.append(x)
  print x

print len(''.join(li))
