import myfunc

count = 0
for i in range(2,100):
  if myfunc.is_prime(i):
    tmp = myfunc.shift_digits(i,1)
    circular = True
    while not tmp == i:
      if not myfunc.is_prime(i):
        circular = False
      tmp = myfunc.shift_digits(tmp, 1)
    if circular:
      count += 1
