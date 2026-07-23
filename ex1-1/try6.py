# ex1-1 - bracket_validator
# attempt: try6.py
# (signature pre-filled from the .en; write your solution below)

def bracket_validator(s: str) -> bool:
    stack = [] # decalre a list of opener brackets
    pairs = { # declare a dictionary of closers and openrs key values
        '}':'{',
        ']':'[',
        ')':'(',
    }
    for bracket in s:
        if bracket in pairs.values(): # it is an opener
            stack.append(bracket) # append to the stack
        elif bracket in pairs.keys(): # it is a closer
            if not stack or pairs[bracket] != stack[-1]: # if stack empty or 
                return False
            stack.pop()

    return len(stack) == 0

# print(bracket_validator("()[]{}")  ) #-> True
# print(bracket_validator("([{}])")  ) #-> True
# print(bracket_validator("(]")      ) #-> False
# print(bracket_validator("([)]")    ) #-> False
# print(bracket_validator("")        ) #-> True