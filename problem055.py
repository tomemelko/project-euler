from myfunc import is_palindrome

for i in xrange(10):
  iterCount = 0
  num = i
  while (is_palindrome(num) == False and iterCount < 51):
    print num
    num = int(str(num)[::-1]) + num
