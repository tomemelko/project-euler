from myfunc import is_palindrome

largest = 0
for i in range(100,1000):
  for j in range(100,1000):
    if (is_palindrome(str(i*j))):
      if (i*j > largest):
        largest = i*j
print largest
