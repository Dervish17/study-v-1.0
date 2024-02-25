def brackets(text):
    stack = []
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    for check in text:
        if check in opening:
            stack.append(opening.index(check))
        elif check in closing:
            if stack and stack[-1] == closing.index(check):
                stack.pop()
            else:
                return False
    return not stack


text = '([{}])()<{}>'
print(brackets(text))
