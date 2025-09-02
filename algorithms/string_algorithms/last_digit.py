# list comprehension example
# new_list = [expression(i) for i in iterable if filter(i)]
print([c for c in "selftaught" if ord(c) > 102])


# Time complexity: O(n)
# Space complexity: O(1)


def last_digit(s1):
    return [c for c in s1 if c.isdigit()][-1]


print(last_digit("Buy 1 get 3 free"))  # 3
