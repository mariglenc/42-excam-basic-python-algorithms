
def bracket_validator(s:str)->bool:
    stack = [] # define an empty list - it will have only the opener brackets
    pairs = {  # define a dictionary with opener values and closing keys of brackets to check
        '}':'{',
        ')':'(',
        ']':'[',
    }

    for char in s: # iterate over the input string
        if char in pairs.values(): # check if the char is an opener
            stack.append(char) # if so append it to the stack
        elif char in pairs.keys(): # check if the char is a closer
            if not stack or stack[-1] != pairs[char]: # check if stack is empty, OR the innermost opener(stack[-1]) differs from the one closer (char) it needs
                return False # return false and stop the iteration 
            stack.pop() # if closer matches the opener then pop it from stack
    
    return len(stack) == 0 # return True if len of stack is 0


print("{()} ->",bracket_validator("{()}"))
print("{(} ->",bracket_validator("{(}"))
print("{((())} ->",bracket_validator("{((())}"))
print("{((()))} ->",bracket_validator("{((()))}"))

