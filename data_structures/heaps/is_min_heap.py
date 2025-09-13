def is_min_heap(tree):
    n = len(tree)

    # Verify each parent node is smaller than it's children
    for i in range((n // 2) - 1, -1, -1):
        if tree[i] > tree[2 * i + 1]:
            return False
        if 2 * i + 2 < n and tree[i] > tree[2 * i + 2]:
            return False
    return True


tree = [10, 15, 14, 25, 30]
print(is_min_heap(tree))  # True

tree = [30, 56, 22, 49, 30, 51, 2, 67]
print(is_min_heap(tree))  # False
