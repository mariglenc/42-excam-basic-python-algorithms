
def bracket_validator(s: str) -> bool:
    stack = []  # list of openers
    pairs = {   # dictionary of closer and opener 
        '}':'{',
        ')':'(',
        ']':'[',
    }

    for char in s:
        if char in pairs.values(): # if is an opener: 
            stack.append(char) # append to the stack
        elif char in pairs.keys(): # if is a closer:
            if not stack or stack[-1] != pairs[char]: # fail if stack empty or top doesn't match, else pop
                return False 
            stack.pop()
    
    return len(stack) == 0


print("{()} ->",bracket_validator("{()}"))
print("{(} ->",bracket_validator("{(}"))
print("{((())} ->",bracket_validator("{((())}"))
print("{((()))} ->",bracket_validator("{((()))}"))