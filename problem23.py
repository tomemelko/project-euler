import myfunc

n = 28123
list = range(1,n)
sum = 0
abund = set()
for i in list:
  if (myfunc.divisors_count(i) > i):
    abund.add(n)
  for a in abund:
    if not (n-a in abund):
      sum += i
      

print sum
