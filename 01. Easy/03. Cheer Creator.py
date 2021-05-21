"""
At the game you cheer:
- "High five" if your team gains more than 10 yards
- "Ra!" for every yard your team gains between 1 and 10 yards
- "shh" if your team loses yards
"""

while True:
    try:
        yards = int(input("How many yards did your team gained? "))

        if yards > 10:
            print("High Five")
        elif 1 <= yards <= 10:
            print("Ra!" * yards)
        else:
            print("shh")
        break
    except ValueError:
        print("Error: Please enter a number.")
