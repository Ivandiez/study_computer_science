def check_parenthesis(a_string):
    stack_paranthesis = []
    stack_brackets = []
    for c in a_string:
        if c == "(":
            stack_paranthesis.append(c)
        if c == ")":
            if len(stack_paranthesis) == 0:
                return False
            else:
                stack_paranthesis.pop()
        if c == "{":
            stack_brackets.append(c)
        if c == "}":
            if len(stack_brackets) == 0:
                return False
            else:
                stack_brackets.pop()
    return len(stack_paranthesis) == 0 and len(stack_brackets) == 0


a_st = "{{{{)))}}})"
print(check_parenthesis(a_st))  # False

a_st_1 = ")()("
print(check_parenthesis(a_st_1))  # False

print(check_parenthesis("(()){}{{}}()"))  # True
