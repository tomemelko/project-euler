import myfunc

sum = 0
for i in range(1,1000000):
  if (myfunc.is_palindrome(str(i))):
    if (myfunc.is_palindrome(bin(i)[2:])):
      sum += i
print sum
