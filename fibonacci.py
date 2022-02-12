""" Python Generator sample script
    Generate Fibonacci series """
def fib_generator(n):
    a=1
    b=1
    for num in range(n):
        yield a
        a,b=b,a+b
for num in fib_generator(10):
    print(num)
