power = 5
total = 0

for i in range(2,1000000):
  sum = 0
  stri = str(i)
  for d in stri:
    sum += (int(d)**power)
    
  if (sum == i):
    total += i
  

print total
