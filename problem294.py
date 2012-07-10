#Time complexity: O(len(n))
def test(n):
  total = 0
  while (n != 0):
    if (total > 23):
      return False  
    total, n = total + n%10,n/10
  if (total == 23):
    return True
  return False

#Time complexity: O((10^n)*(len(k))
#Since len(k) = n in the worst case (which is also the best case in this implementation)
#Time complexity: O(n*(10^n)) 
#Exponential time... There has got to be a better way to do this.
def s(n):
  count = 0
  for k in xrange(2300,10**n,23):
    #if (k % 10**(n-2) == 0):
      #print float(k)/10**(n-2)
    if (test(k)):
      count += 1
  return count

print s(9)
