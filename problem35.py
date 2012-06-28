import myfunc

count = 0
print "Creating list"
plist = myfunc.prime_list(1000000)
print "Finished"
for i in plist:
  tmp = myfunc.shift_digits(i, 1)
  circ = True
  print "i=",i
  while not tmp == i:
    print tmp
    if not tmp in plist:
      circ = False
    tmp = myfunc.shift_digits(tmp, 1)
  if circ:
    count += 1
print count
