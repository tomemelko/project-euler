from myfunc import prime_list

sum = 0
for i in prime_list():
  if (i > 2000000):
    break
  sum += i
print sum
