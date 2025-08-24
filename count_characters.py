def count_characters(string):
    # Time complexity: O(n)
    # Space complexity: O(n)
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)

count_characters("Supermassive")
