'''Find PI to the Nth Digit - Enter a number and
have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.'''
from math import pi
def display(places):
    """ print PI with user defined decimal points"""
    print(f'{pi:1.{places}f}')
N=100
while (N>=100):
    N=int(input("Enter the number of decimal places: "))
    if (N>=100):
        print("Enter a number less than 100")
    else:
        display(N)

