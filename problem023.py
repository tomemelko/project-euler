import myfunc

n = 28123
sum = 0
abund = set()
for i in range(1,n):
  if (myfunc.divisors_count(i) > i):
    abund.add(i)
###### Orignal code, doesn't work #####
##  for a in abund:
##    if not (i-a in abund):
##      sum += i

  if not any( (i-a in abund) for a in abund ):
    sum += i


print sum
