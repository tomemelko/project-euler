from myfunc import is_prime, is_pandigital
max = 0
for i in xrange(1000000001,1,-2):
  if (is_pandigital(i, len(str(i)))):
    if (is_prime(i)):
    #if (is_pandigital(i, len(str(i)))):
      print i
      exit()
