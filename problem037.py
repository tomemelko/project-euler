from myfunc import is_prime

sum = 0
count = 0
for n in range(9,1000000):
  trunc = True
  i = n
  if count == 11:
    break
  while len(str(i)) != 0:
    if not is_prime(i):
      trunc = False
      break
    if len(str(i)) == 1:
      break
    i = int(str(i)[1:])
  i = n
  while len(str(i)) != 0:
    if not is_prime(i):
      trunc = False
      break
    if len(str(i)) == 1:
      break
    i = int(str(i)[:-1])
                              
  if trunc:
    print n
    sum += n
    count += 1
print sum
print count
