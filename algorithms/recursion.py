# Non-recursive factorial function
def factorial_non_rec(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n -= 1
    return the_product


print(factorial_non_rec(5))


# recursion factorial function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def return_nums(n):
    """Return numbers from 1 to n using recursion"""
    if n:
        return_nums(n - 1)
    else:
        return None
    print(f"{n}")


return_nums(10)
