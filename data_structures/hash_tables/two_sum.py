# Time complexity: O(n**2)
# Space complexity: O(1)
def two_sum_brute(the_list, target):
    index_list = []
    for i in range(0, len(the_list)):
        for j in range(i, len(the_list)):
            if the_list[i] + the_list[j] == target:
                index_list.append((i, j))
    return index_list


lst = [-1, 2, 3, 4, 7]
target = 5
print(two_sum_brute(lst, target))


# Time complexity: O(n)
# Space complexity: O(n)
def two_sum(a_list, target):
    a_dict = {}
    for index, n in enumerate(a_list):
        rem = target - n
        if rem in a_dict:
            return index, a_dict[rem]
        else:
            a_dict[n] = index
    return None


lst = [-1, 2, 3, 4, 7]
target = 5
print(two_sum(lst, target))
