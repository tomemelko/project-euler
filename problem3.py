import math
from myfunc import is_prime

n = 600851475143
for i in range(3,int(math.sqrt(n)),2):
  if (n % i == 0):
    if (is_prime(i)):
      print i
