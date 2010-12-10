import time

def memoize(f):
  memo = {}
  def _memoize(*args, **kwargs):
    try:
      return memo[args]
    except KeyError:
      r = f(*args, **kwargs)
      memo[args] = r
      return r
  _memoize.func_name = f.func_name
  return _memoize

def timer(f):
  def _timer(*args):
    start = time.time()
    r = f(*args)
    stop = time.time()
    print "%s took %s secs to execute." % (f.func_name, str(stop - start))
    return r
  _timer.func_name = f.func_name
  return _timer


@memoize
def fib(n):
  if n == 0 or n == 1: return 1
  return fib(n-1) + fib(n-2)
