def check_parentheses(a_string):
    stack = []
    for c in a_string:
        if c == "(":
            stack.append(c)
        if c == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


a_st = "()()()"
print(check_parentheses(a_st))  # True

a_st_1 = ")()("
print(check_parentheses(a_st_1))  # False
