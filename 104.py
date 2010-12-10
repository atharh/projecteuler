from mine import memoize

def ispand19(n):
  s = ''.join(sorted(list(str(n))))
  return s == "123456789"

@memoize
def fib(n):
  """ Efficient fib.

  fib(2n-1) = fib(n-1)^2 + fib(n)^2
  fib(2n) = fib(n)(2fib(n-1) + fib(n))
  """
  if n <= 1: return 1
  if n % 2 == 0:
    return fib(n/2) * (2 * fib(n/2-1) + fib(n/2))
  else:
    return fib(n/2-1)**2 + fib(n/2)**2


for i in range(15):
  fib(2*i)
  print i, fib(i)
