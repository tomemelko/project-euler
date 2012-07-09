import operator
import math

def is_prime(n):
  if (n == 1):
    return False
  if (n == 2):
    return True
  if (n % 2 == 0):
    return False
  for i in range(3, int(n**.5)+1, 2):
    if (n % i == 0):
      return False
  return True

def fibonacci(n1, n2, limit):
  while n2 < limit:
    yield n2
    n1, n2 = n2, n1+n2
  
def divisors(n):
  for i in range(1,(n/2)+1):
    if (n % i == 0):
      yield i      
    
def divisors_count(n):
  count = 2
  for i in range(2, int(math.floor(n**.5))):
    if (n % i == 0):
      count += 2
      if (n / i == i):
        count -=1
  return count

def prime_factors(n):
  for i in prime_list():
    if (i > n):
      break
    while (n % i == 0):
      yield i
      n = n / i
                
def perfect_numbers(n):
  for i in xrange(1,n):
    if (divisors_count(i) == i):
      yield i

def abundant_numbers(n):
  for i in xrange(n):
    if (sum(divisors(i)) > i):
      yield i

def shift_digits(n, dist):
  return n[dist:] + n[:dist]
  
def sum_of_digits(n):
  sum = 0
  for i in str(n):
    sum += int(i)
  return sum
    
def prime_list(n):
  #Note, this is a generator
  #Sourced from:
  #http://stackoverflow.com/a/568618
  D = {}
  q = 2
  while True:
    if q > n:
      break
    if q not in D:
      yield q
      D[q * q] = [q]
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      del D[q]
    q += 1

def is_palindrome_slow(n):
  if len(n) == 1:
    return True
  for i in range((len(n)/2)+1):
    if n[i] != n[len(n)-i-1]:
      return False
    
  return True
  
def is_palindrome(n):
  if n[::-1] == n:
    return True
  return False

def lcm(a):
  res = []
  for i in a:
    factors = prime_factors(i)
    for j in factors:
      while (res.count(j) < factors.count(j)):
        res.append(j)
  return reduce(operator.mul, res)

def triangle(n):
  return (n+1)*n/2

def collatz(n):
  while (n != 1):
    if (n%2==0):
      n = n/2
    else:
      n = (3*n)+1
    yield n

def collatz_count(n):
  count = 0
  while (n != 1):
    if (n%2==0):
      n = n/2
    else:
      n = (3*n)+1
    count += 1
  return count      

def collatz_count_cached(q,n): #Returns a dict with all the numbers from q to n
  cache = dict()
  for i in xrange(q,n):
    step = collatz(i).next()
    if (step in cache):
      cache[i] = cache.get(step) + 1
    else:
      cache[i] = collatz_count(i)
  return cache

def is_pandigital(n, length):
  if (len(str(n)) != length):
    return False
  for i in xrange(1,length+1):
    if (str(n).count(str(i)) != 1):
      return False
  return True
