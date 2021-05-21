"""
You visit n houses on Halloween. One of the houses gives you a toothbrush, two of the houses give you
a dollar bill and the rest of the houses give you a candy.

Calculate the chance (in %) of pulling a dollar bill from your bag.

Round up the result to the nearest whole number.

Constrains:
house >= 3
"""

import math

while True:
    try:
        houses = int(input("How many houses did you visit? "))

        percentage = math.ceil(100 / (houses / 2))

        print(f"The chance of pulling a dollar bill from your bag is {percentage}%.")
        break

    except ValueError:
        print('Error: Please enter a number.')
