# Time complexity: O(logn)
# Space complexity: O(1)

def exponent_of_two(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count

print(exponent_of_two(16))
print(exponent_of_two(32))
