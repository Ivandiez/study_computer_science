# Use this when our list is sorted (or sort before use)
# Time complexity: O(log n)
# Space complexity: O(1)
def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


lst = [0, 2, 3, 4, 5, 6, 9, 10, 12, 39, 40, 55]
print(binary_search(lst, 39))  # True
print(binary_search(lst, 11))  # False


# Built-in Python Binary Search function
from bisect import bisect_left

sorted_fruits = ['apple', 'banana', 'cherry', 'plum']
print(bisect_left(sorted_fruits, 'banana'))  # 1
print(bisect_left(sorted_fruits, 'blueberry'))  # 2 (since it should be after banana and before cherry)

# Real-world usage of bisect_left (how to use)
def binary_search_bisect(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if index <= len(an_iterable) and an_iterable[index] == target:
        return True
    return False

print(binary_search_bisect(sorted_fruits, 'banana'))  # True
print(binary_search_bisect(sorted_fruits, 'blueberry'))  # False


# Binary search chars in list of chars in alphabet order
def binary_search_string(an_iterable, find):
    first = 0
    last = len(an_iterable) - 1
    target_code = ord(find)
    while last >= first:
        mid = (first + last) // 2
        if an_iterable[mid] == find:
            return True
        else:
            if target_code < ord(an_iterable[mid]):
                last = mid - 1
            else:
                first = mid + 1
    return False

print(binary_search_string(['a', 'b', 'c', 'd'], 'c'))  # True
print(binary_search_string(['a', 'b', 'c', 'd'], 'e'))  # False
