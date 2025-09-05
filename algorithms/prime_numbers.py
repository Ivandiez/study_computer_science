# Time complexity: O(n)
# Space complexity: O(1)
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(11))  # True
print(is_prime(15))  # False


# Faster algorithm
import math


# Time complexity: O(sqrt(n))
# Space complexity: O(1)
def is_prime_faster(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime_faster(28))  # False
print(is_prime_faster(31))  # True


# To output list of prime numbers until n
# Time complexity: O(n**2)
# Space complexity: O(n)
def find_primes(n):
    return [i for i in range(2, n) if is_prime_faster(i)]


print(find_primes(50))  # List of prime numbers up to 50
