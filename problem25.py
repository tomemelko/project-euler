import myfunc

fib = myfunc.fibonacci(1,1,10**1001)
for i in fib:
  if (len(str(i)) > 1000):
    print fib.index(i)
