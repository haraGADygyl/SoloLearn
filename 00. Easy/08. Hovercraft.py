"""
Determine if you made a profit making hovercrafts this month. You make 10 hovercrafts per month.

Each hovercraft costs 2 000 000 to make.
Each hovercraft sells for 3 000 000.
Insurance per month costs 1 000 000.
"""

while True:
    try:
        hovercrafts_sold = int(input("How many hovercrafts have you sold? "))

        total = hovercrafts_sold * 3000000 - 21000000

        if total < 0:
            print("Loss")
        elif total == 0:
            print("Broke Even")
        else:
            print("Profit")
        break
    except ValueError:
        print("Error: Please enter a number.")
