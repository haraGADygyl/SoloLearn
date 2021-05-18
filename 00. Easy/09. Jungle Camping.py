"""
Based on the noises you hear, determine what the animals are.
"""

noises = [x for x in input("What noises do you hear? ").split()]

for noise in noises:
    if noise == 'Grr':
        print("Lion", end=" ")
    elif noise == "Rawr":
        print("Tiger", end=" ")
    elif noise == "Ssss":
        print("Snake", end=" ")
    elif noise == "Chirp":
        print("Bird", end=" ")
