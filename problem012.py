from myfunc import divisors_count, triangle

for i in xrange(100000):
  tri = triangle(i)
  if (divisors_count(tri) > 500):
    print tri
    break
