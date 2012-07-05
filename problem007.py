from myfunc import prime_list
from itertools import islice

print islice(prime_list(), 10001, 10002).next()
