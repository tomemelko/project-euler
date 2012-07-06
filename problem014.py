#Collatz problem! YAY
from myfunc import collatz_count_cached

a = collatz_count_cached(500000,1000000)
print max(a, key=a.get)
