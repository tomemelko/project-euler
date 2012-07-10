from myfunc import sum_of_digits

def s(n):
  count = 0
  for k in xrange(2300,10**n,23):
    if (k % 10**(n-2) == 0):
      print k
    if (sum_of_digits(k) == 23):
      count += 1
  return count

print s(9)
