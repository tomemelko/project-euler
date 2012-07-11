from myfunc import sum_of_digits

count = 0
for i in xrange(10**9):
  if (sum_of_digits(i) == sum_of_digits(137*i)):
    count += 1
print count
