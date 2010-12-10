def firstdenom(k):
  l = [1, 2, 5, 10, 20, 50, 100, 200]
  return l[k-1]


def cc(amount, k):
  if amount == 0: return 1
  elif amount < 0 or k == 0: return 0
  else:
    return cc(amount, k-1) + cc(amount-firstdenom(k), k)


print cc(200, 8)
