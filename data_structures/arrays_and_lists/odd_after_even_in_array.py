import array


# Time complexity: O(n)
# Space complexity: O(n)
def return_prime_after_non_prime(an_arr):
    odd_arr = array.array("i", [])
    even_arr = array.array("i", [])
    for i in range(len(an_arr) - 1):
        if an_arr[i] % 2 == 0:
            even_arr.append(an_arr[i])
        else:
            odd_arr.append(an_arr[i])
    return even_arr + odd_arr


arr = array.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(return_prime_after_non_prime(arr))  # array('i', [2, 4, 6, 8, 1, 3, 5, 7, 9])
