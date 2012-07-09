from myfunc import triangle,is_pentagonal,is_hexagonal

for i in xrange(500000):
  n = triangle(i)
  if (is_pentagonal(n) and is_hexagonal(n)):
    if (n > 40755):
      print n
      break
