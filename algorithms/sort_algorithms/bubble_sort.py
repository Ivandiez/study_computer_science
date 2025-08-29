# Time complexity: O(n**2), in best case O(n)
# Space complexity: O(1)

def bubble_sort(a_list):
    list_length = len(a_list)
    for i in range(list_length - 1):
        no_swaps = True
        for j in range(list_length - i - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False
            if no_swaps:
                return a_list
    return a_list


lst = [9, 1, 32, 10]
print(bubble_sort(lst))
