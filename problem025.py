import myfunc

fib = myfunc.fibonacci(1,0,10**1000)
for i in fib:
  if (len(str(i)) == 1000):
    print fib.index(i),len(str(i))
