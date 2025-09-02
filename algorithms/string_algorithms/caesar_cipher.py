# Time complexity: O(n)
# Space complexity: O(1)

import string


def cipher(a_string, key):
    # To create lists of uppercase and lowercase letters
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt = ""

    for c in a_string:
        if c in uppercase:
            # Use modular to correctly calculate when index is greater than 25
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt


print(cipher("Hello, World!", 3))  # Khoor, Zruog!
