for i in xrange(0,500000000):
  ans = True
  for j in xrange(1,20):
    if (i % j != 0):
      ans = False
  if ans:
    print i
