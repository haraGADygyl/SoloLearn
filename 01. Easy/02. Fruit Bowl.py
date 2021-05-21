"""
You have a bowl with even number of bananas and apples in it. For one apple pie you need 3 apples.

Calculate the number of pies you can make.
"""

while True:
    try:
        fruits = int(input("How many fruits you have in the basket? "))

        pies = int((fruits / 2) / 3)

        print(f"You can make {pies} apple pies.")
        break
    except ValueError:
        print("Error: Please enter a number.")
