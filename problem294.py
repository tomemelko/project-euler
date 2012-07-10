def test(n):
  total = 0
  while (n != 0):
    if (total > 23):
      return False
    total, n = total + n%10,n/10
  if (total == 23):
    return True
  return False

def s(n):
  count = 0
  for k in xrange(2300,10**n,23):
    if (k % 10**(n-2) == 0):
      print float(k)/10**(n-2)
    if (test(k)):
      count += 1
  return count

print s(9)
