# Solution with linear time
# Time complexity: O(n)
# Space complexity: O(1)
def gcf(i1, i2):
    if i1 < 0 or i2 < 0:
        raise ValueError("Numbers must be positive")

    if i1 == 0:
        return i2
    if i2 == 0:
        return i1

    if i1 > i2:
        smaller = i2
    else:
        smaller = i1

    for divisor in range(1, smaller + 1):
        if i1 % divisor == 0 and i2 % divisor == 0:
            gcf = divisor

    return gcf


print(gcf(20, 12))
print(gcf(0, 22))


# Euclid algorithm
# Time complexity: O(logn)
# Space complexity: O(1)
def euclid_gcf(x, y):
    if y == 0:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


print(euclid_gcf(20, 12))
print(euclid_gcf(0, 22))
