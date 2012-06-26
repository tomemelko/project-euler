import myfunc

list = range(1,28123)
abund = myfunc.abundant_numbers(28123)
for i in abund:
  for j in abund[i:]:
    if (i+j in list):
      list.remove(i+j)
      
      
      

print sum(list)
