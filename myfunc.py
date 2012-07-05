import math

def is_prime(n):
  if (n == 1):
    return False
  if (n == 2):
    return True

  if (n % 2 == 0):
    return False

  for i in range(3, int(math.sqrt(n))+1, 2):
    if (n % i == 0):
      return False

    
  return True


def fibonacci(n1, n2, limit):
  list = []
  while n2 < limit:
    #print "Adding ",n2
    #print "Is the", len(list), "th term with length", len(str(n2))
    list.append(n2)
    n1, n2 = n2, n1+n2

  return list
  
def divisors(n):
  list = []
  for i in range(1,(n/2)+1):
    if (n % i == 0):
      list.append(i)
      
    
  return list

def divisors_count(n):
  count = 1
  for i in range(2, int(math.sqrt(n))+1):
    if (n % i == 0):
      count += i + n / i
      
      
  if (math.sqrt(n) == int(math.sqrt(n))):
    count -= math.sqrt(n)
    
  return count

def prime_factors(n):
  list = []
  for i in prime_list():
    if (i > n):
      break
    while (n % i == 0):
      list.append(i)
      n = n / i
  return list
                

def perfect_numbers(n):
  list = []
  for i in range(1,n):
    if (divisors_count(i) == i):
      list.append(i)

  
  return list

def abundant_numbers(n):
  list = []
  for i in range(1,n):
    if (len(list) != 0):
      if (list[0] + list[-1] >= n):
        break
      
      
    if (divisors_count(i) > i):
      list.append(i)


  return list

def shift_digits(n, dist):
  return n[dist:] + n[:dist]
    
def prime_list():
  #Note, this is a generator
  #Sourced from:
  #http://stackoverflow.com/a/568618
  D = {}
  q = 2
  while True:
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
