import array

# Time complexities for:
# Access: O(1)
# Search: O(n)
# Insertion: O(n)
# Deletion: O(n)
arr = array.array("f", [1.0, 1.5, 2.0, 2.5])
print(arr[1])

arr[1] = "hello"  # TypeError: array item must be a float
