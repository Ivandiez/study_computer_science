def ss(number_list, n):
    # Time complexity: O(n)
    # Space complexity: O(1)
    for i in number_list:
        if i == n:
            return True
    return False

numbers = range(0, 100)
ss1 = ss(numbers, 2)
print(ss1)
ss2 = ss(numbers, 202)
print(ss2)
