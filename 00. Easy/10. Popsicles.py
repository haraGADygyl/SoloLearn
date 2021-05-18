"""
Determine whether you can give each of your siblings equal number of popsicles.
If not, eat them yourself.
"""

while True:
    try:
        siblings = int(input("How many siblings do you have? "))
        popsicles = int(input("How many popsicles do you have? "))

        if siblings % popsicles:
            print("give away")
        else:
            print("eat them yourself")
        break
    except ValueError:
        print("Error: Please enter a number.")
