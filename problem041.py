from myfunc import is_prime
from itertools import permutations
max = 0
#Since all 9-pandigital numbers will sum to 45, and therefore are divisible by 3
#And the samething goes for 8 digit pandigital numbers, as they sum to 36
#We only need to go up to 7 digits
for i in permutations(['1','2','3','4','5','6','7']):
  num = ''.join(i)
  if (is_prime(int(num))):
    if (num > max):
      max = num
print max
