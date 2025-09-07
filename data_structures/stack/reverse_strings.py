# To reverse string we can use
st = "ofdspgosd"
print(st[::-1])
# Or
print("".join(reversed(st)))


# And we can use stack to reverse the string
def reverse_string(a_string):
    stack = []
    string = ""
    for c in a_string:
        stack.append(c)
    for c in a_string:
        string += stack.pop()
    return string


print(reverse_string(st))
