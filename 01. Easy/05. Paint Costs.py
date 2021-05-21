"""
Based on the total number of colors you need, calculate the cost of your project.

The canvas and brushes cost 40, each color costs 5 and the tax is 10%

Round up the result to the nearest whole number.
"""

import math

while True:
    try:
        colors_needed = int(input("How many colors do you need? "))

        result = colors_needed * 5 + 40
        result_plus_tax = result + result * 0.1

        print(f"The total cost of your project is {math.ceil(result_plus_tax)}")
        break
    except ValueError:
        print("Error: Please enter a number.")
