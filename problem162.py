import itertools
count = 0
for i in itertools.count(0):
  if (len(hex(i)) > 16):
    break
  hexI = hex(i)[2:]
  if ('1' in hexI and '0' in hexI and 'a' in hexI):
    count += 1
print hex(count)
