
def bracket_validator(s:str)->bool:
    stack = [] # define an empty list - stack of openers
    pairs = { # define a dictionary of closer → opener bracket pairs
        ']':'[',
        ')':'(',
        '}':'{',
    }

    for char in s: # iteratote over all chars of incoming string
        if char in pairs.values(): # if char is opener
            stack.append(char) # append to the stack
        elif char in pairs.keys(): # if char is closer
            if not stack or stack[-1] != pairs[char]: # if stack is empty or the innermost one is not correct
                return False # stop the iteration and return false
            stack.pop() # else remove the opener from stack

    return len(stack) == 0 # return true if stack empty

print("{()} ->",bracket_validator("{()}"))
print("{(} ->",bracket_validator("{(}"))
print("{((())} ->",bracket_validator("{((())}"))
print("{((()))} ->",bracket_validator("{((()))}"))