"""
Determine if you need to call Batman for help, based on the number of criminals reported.
"""

while True:
    try:
        criminals_count = int(input("How many criminals are reported? "))

        if criminals_count < 5:
            print("I got this!")
        elif 5 <= criminals_count <= 10:
            print("Help me Batman")
        else:
            print("Good Luck out there!")
        break
    except ValueError:
        print("Error: Please enter a number.")
