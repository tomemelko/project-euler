from myfunc import is_palindrome

count = 0
for i in xrange(10000):
  iterCount = 0
  num = int(str(i)[::-1]) + i #First step must happen outside of loop, so that we can avoid initial palindromes
  while (is_palindrome(str(num)) == False and iterCount < 51):
    num = int(str(num)[::-1]) + num
    iterCount += 1
  if iterCount > 50:
    count += 1
print count
