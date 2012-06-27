import math

def is_prime(n):
  if (n == 1 or n == 2):
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
