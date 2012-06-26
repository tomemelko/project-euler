def is_prime(n):
  if (n % 2 == 0):
    return false

  for i in range(3, math.sqrt(n), 2):
    if (n % i == 0):
      return false
    
    return true


