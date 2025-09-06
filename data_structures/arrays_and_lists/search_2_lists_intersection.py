# Time complexity: O(n**2)
# Space complexity: O(n)
def return_inter(list1, list2):
    list3 = [v for v in list1 if v in list2]
    return list3


list1 = [2, 43, 58, 62, 68, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
print(return_inter(list1, list2))


# We can use `set` and it's `intersection` function to solve the task
def return_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))


list1 = [2, 43, 58, 62, 68, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
new_list = return_intersection(list1, list2)
print(new_list)

# We can use intersection to search common elements
# (s1.intersection(s2, s3, s4))
