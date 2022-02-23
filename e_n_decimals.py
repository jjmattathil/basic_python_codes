"""Find e to the Nth Digit -
Enter a number and have the program generate e up to that many decimal places.
 Keep a limit to how far the program will go."""
from math import e
def display(places):
    """ print e with user defined decimal points"""
    print(f'{e:1.{places}f}')
N=100
while (N>=100):
    N=int(input("Enter the number of decimal places: "))
    if (N>=100):
        print("Enter a number less than 100")
    else:
        display(N)
