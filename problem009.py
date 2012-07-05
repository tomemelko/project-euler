for a in range(1,500):
  for b in range(1,500):
    c = ((a**2)+(b**2))**.5
    if (c == int(c)):
      if (a+b+c == 1000):
        print a*b*c
        exit()
