# Time complexity: O(nlogn)
# Space complexity: O(1)


def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


s1 = "Emperor Octavian"
s2 = "Captain over Rome"
print(is_anagram(s1, s2))
