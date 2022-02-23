"""Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them."""
def prime_fact(Number):
    my_list=[]
    for i in range(2,Number):
        if Number%i==0:
            my_list.append(i)
    if(len(my_list)==0):
        my_list.append(Number)
    print(my_list)

N=int(input("Please enter the Number from 2 to any: "))
prime_fact(N)