"""
Decode the message by removing all non-letter and non-space characters and reverse the string.
"""

import re

message = input("Enter the encrypted message here: ")

pattern = "[a-zA-Z ]"

result = re.findall(pattern, message)

print("The decoded message is: ", "".join(result[::-1]))
