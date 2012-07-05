sqOfSum = sum(xrange(1,101))**2
sumOfSq = 0

for i in xrange(1,101):
  sumOfSq += i**2
print sqOfSum-sumOfSq
