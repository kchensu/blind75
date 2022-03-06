def validParentheses(s):
    stack = []
    dictionary = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if stack and dictionary[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return not stack


s = "()[]{}"
print(validParentheses(s))
