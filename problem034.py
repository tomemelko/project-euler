from math import factorial

total = 0

for i in range(3,1000000):
  sum = 0
  for d in str(i):
    sum += factorial(int(d))
  if (sum == i):
    print i,"is awesome"
    total += i
    
    
  

print total
