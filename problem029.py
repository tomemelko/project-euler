alim = 101
blim = 101

set = set()

for a in range(2,alim):
  for b in range(2,blim):
    if not a**b in set:
      set.add(a**b)
      
print len(set)
