"""
Remove any symbols from the string, except letters, numbers and spaces.
"""

import re

message = input("Enter the random symbols text here: ")

pattern = "[a-zA-Z0-9 ]"

result = re.findall(pattern, message)

print("The non-symbols text is: ", "".join(result))
