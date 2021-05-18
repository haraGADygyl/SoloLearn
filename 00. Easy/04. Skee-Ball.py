"""
You gain 1 ticket for every 12 points you score.

Calculate whether you can buy the squirt gun in the game.
"""

while True:
    try:
        points = int(input("How many points did you score? "))
        cost = int(input("How many tickets does the squirt gun cost? "))

        result = points // 12

        if result >= cost:
            print("Buy it!")
        else:
            print("Try again")
        break
    except ValueError:
        print("Error: Please enter a number.")
