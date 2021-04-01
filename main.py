def isBalanced(s):
    closing_brackets = ["}", "]", ")"]
    stack = []
    
    for char in s:
        if char in closing_brackets:
            # closed without opening
            if not stack:
                return "NO"

            last_opening_bracket = stack.pop()
            if not didMatch(last_opening_bracket, char):
                return "NO"
        else:
            # append opening brackets
            stack.append(char)
    # if stack is not empty is because that the bracket was opened but      not closed
    return "NO" if stack else "YES"

def didMatch(opening_bracket, closing_bracket):
    if opening_bracket == "{" and closing_bracket == "}" or \
        opening_bracket == "[" and closing_bracket == "]" or \
        opening_bracket == "(" and closing_bracket == ")":
        return True
    return False
