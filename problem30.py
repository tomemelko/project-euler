power = 5
total = 0

for i in range(2,200000): #limit is 200,000 because that's greater than the largest such number, only changed to improve running time
  sum = 0
  stri = str(i)
  for d in stri:
    sum += (int(d)**power)
    
  if (sum == i):
    total += i
  

print total
