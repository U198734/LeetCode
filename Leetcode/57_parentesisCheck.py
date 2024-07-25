def isValid(s):
    # Dictionary to hold the matching pairs of brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of the opening brackets
    stack = []
    
    # Loop through each character in the string
    for char in s:
        if char in bracket_map:
            # Pop the top element from the stack if it is not empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it to the stack
            stack.append(char)
    
    # If the stack is empty, all the opening brackets have been matched correctly
    return not stack

# Examples
print(isValid("()"))        # Output: True
print(isValid("()[]{}"))    # Output: True
print(isValid("(]"))        # Output: False