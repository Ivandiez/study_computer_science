# We can use it if our data is unsorted list
# Time complexity: O(n). In best case (first element match): O(1),
# In mean: O(n/2)
# Space complexity: O(1)
def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False


a_list = [1, 8, 30, 90, 5, 102, 20, 3, 9]
print(linear_search(a_list, 90))  # True
print(linear_search(a_list, 100))  # False


# Built-in linear_search in Python is using keyword 'in'
unsorted_list = [1, 45, 3, 32, 3]
print(45 in unsorted_list)  # True
print(100 in unsorted_list)  # False
print("a" in "apple")  # True
