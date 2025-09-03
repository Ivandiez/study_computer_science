def is_even(n):
    # Since bitwise AND with 1 checks the least significant bit
    # we use it to determine if a number is even
    # For example: (2) 0b10 & 0b01 = 0, (3) 0b11 & 0b01 = 1
    return not n & 1


print(is_even(4))  # True
print(is_even(5))  # False


def is_power_of_two(n):
    # Since bitwise AND between n and n-1 will be 0 only if n is a power of 2
    # For example: (4) 0b100 & 0b011 = 0, (5) 0b101 & 0b100 = 4
    if n & (n - 1) == 0:
        return True
    return False


print(is_power_of_two(4))  # True
print(is_power_of_two(5))  # False
