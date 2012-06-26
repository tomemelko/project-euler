sum, a, b = 0, 0, 1
while b < 4000000:
  if (b % 2):
    sum += b

  a, b = b, b+a
  
print b
