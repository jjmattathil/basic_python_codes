"""prime nos using Lamdba function"""""
x=10
for n in range(2,x):
    prime_no = (lambda n: all(n % i != 0 for i in range(2, n - 1)))
    if prime_no(n):
        print(n)




