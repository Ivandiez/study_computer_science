a_set = set()
a_set.add("Kanye West")
a_set.add("Elon Musk")
a_set.add("Jeff Bezos")
a_set.add("Kanye West")  # Duplicate, will not be added
print(a_set)


# Time complexity: O(n)
# Space complexity: O(n)
def return_duplicates(an_interable):
    """Return a list of duplicates in the given list."""
    dups = []
    a_set = set()

    for item in an_interable:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if l1 == l2:
            dups.append(item)
    return dups


a_list = ["Kanye West", "Elon Musk", "Jeff Bezos", "Kanye West"]
dups = return_duplicates(a_list)
print(dups)  # ['Kanye West']
