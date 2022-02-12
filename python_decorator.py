""" Pyhton decorator sample code"""
def my_new_func(my_func):
    def ne_code(a,b):
        print("The sum is ")
        print(my_func(a,b))
        print("for a and b")
    return ne_code

@my_new_func
def my_func(a,b):
    return (a+b)

my_func(1,2)
