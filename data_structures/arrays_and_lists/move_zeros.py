# Time complexity: O(n)
# Space complexity: O(1)
def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return a_list


a_lst = [8, 0, 3, 0, 12]
move_zeros(a_lst)
print(a_lst)  # [8, 3, 12, 0, 0]
