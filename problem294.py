from myfunc import sum_of_digits

def s(n):
  isNum = True
  count = 0
  for k in xrange(10**n):
    if (k % 10**(n-2) == 0):
      print k
    if (k % 23 != 0):
      isNum = False
    if (isNum):
      if (sum_of_digits(k) != 23):
        isNum = False
    if (isNum):
      count += 0
  return count

print s(9)
