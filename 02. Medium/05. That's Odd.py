"""
Find the sum of all even integers in a list of numbers.
"""

nums_count = int(input("How many numbers will you enter? "))

total = 0
for _ in range(nums_count):
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        total += num

print(f"The total of all even numbers is {total}.")
