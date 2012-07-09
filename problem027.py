from myfunc import is_prime

bestcount = 0
bestproduct = 0
for n in xrange(0,200):
  for a in xrange(-1000,1000):
    count = 0
    for b in xrange(-1000,1000):
      if (is_prime((n**2)+(a*n)+b)):
        count += 1
    if (count > bestcount):
      bestcount, bestproduct = count, a*b
print best product
