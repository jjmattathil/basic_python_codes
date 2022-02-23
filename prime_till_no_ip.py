"""Next Prime Number - Have the program find prime numbers
until the user chooses to stop asking for the next one."""
def check_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def send_prime(num):
    while True:
        if check_prime(num):
            return num
            break
        else:
            num+=1
num=2
print(num)
while True:
    ip=input("Do you want to continue 'n' or 's? ")
    if(ip=='n'):
        num+=1
        num=send_prime(num)
        print(num)
    else:
        break

