# Time complexity: O(n)
# Space complexity: O(n)
def count(a_string):
    a_dict = {}
    for ch in a_string:
        if ch in a_dict:
            a_dict[ch] += 1
        else:
            a_dict[ch] = 1
    return a_dict


st = "Hello"
print(count(st))
