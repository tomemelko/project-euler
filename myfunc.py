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
    list.append(n2)
    n1, n2 = n2, n1+n2

  return list
