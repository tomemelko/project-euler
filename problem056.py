from myfunc import sum_of_digits

max = 0
for a in xrange(100):
  for b in xrange(100):
    sum = sum_of_digits(a**b)
    if (sum > max):
      max = sum
print max
