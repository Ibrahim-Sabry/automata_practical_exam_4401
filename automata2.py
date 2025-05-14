def is_balanced_parentheses(input_string):
    stack = []

    for char in input_string:
        if char == '(':
            stack.append(char) 
        elif char == ')':
            if not stack:
                return False  
            stack.pop() 

    return len(stack) == 0 

test_cases = ["(())", "(()())", "())(", "((())", ""]

for test in test_cases:
    result = is_balanced_parentheses(test)
    print(f"'{test}' is balanced: {result}")