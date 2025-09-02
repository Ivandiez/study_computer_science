# Time complexity: O(n)
# Space complexity: O(1)


def is_palindrome(s1):
    return s1.lower() == s1[::-1].lower()


print(is_palindrome("Racecar"))
