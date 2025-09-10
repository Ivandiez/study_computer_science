import re


# Time complexity: O(n)
# Space complexity: O(n)
def remove_duplicates(a_string):
    a_dict = {}
    words = re.compile(r"\w+").findall(a_string)
    res_str = ""

    for word in words:
        if word not in a_dict:
            a_dict[word] = 1
            res_str += word + " "
    return res_str.strip()


st = "I am a self-taught programmer looking for a job as a programmer."
print(remove_duplicates(st))
