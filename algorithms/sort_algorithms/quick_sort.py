# Time complexity: O(n * logn), worst case: O(n**2)
# Space complexity: O(n)


def partition(a_list, start, end):
    pivot = a_list[start]
    low = start + 1
    high = end

    while True:
        while low <= high and a_list[high] >= pivot:
            high -= 1
        while low <= high and a_list[low] <= pivot:
            low += 1

        if low <= high:
            a_list[low], a_list[high] = a_list[high], a_list[low]
        else:
            break

    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


def quick_sort(a_list, start, end):
    if start >= end:
        return

    pivot_index = partition(a_list, start, end)
    quick_sort(a_list, start, pivot_index - 1)
    quick_sort(a_list, pivot_index + 1, end)

    return a_list


print(quick_sort([5, 2, 9, 3], 0, len([5, 2, 9, 3]) - 1))
