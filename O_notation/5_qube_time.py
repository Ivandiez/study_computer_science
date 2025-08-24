# Time complexity: O(n**3)
# Space complexity: O(1)
nums = [1, 2, 3, 4, 5]
for i in nums:
    for j in nums:
        for k in nums:
            x = i + j + k
            print(x)
