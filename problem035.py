import myfunc

count = 0
for i in myfunc.prime_list():
  if i > 1000000:
    break
  tmp = myfunc.shift_digits(str(i), 1)
  circ = True
  while int(tmp) != i:
    if not myfunc.is_prime(int(tmp)):
      circ = False
    tmp = myfunc.shift_digits(tmp, 1)
  if circ:
    count += 1
print count
