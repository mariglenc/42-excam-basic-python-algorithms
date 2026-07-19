
def bracket_validator(s: str)-> bool:
    stack = []
    list = {
        '}':'{',
        ']':'[',
        ')':'(',
    }

    for char in s:    
        if char in list.values():
            stack.append(char)
        elif char in list.keys():
            if not stack or stack[-1] != list[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

print("{()} ->",bracket_validator("{()}"))
print("{(} ->",bracket_validator("{(}"))
print("{((())} ->",bracket_validator("{((())}"))
print("{((()))} ->",bracket_validator("{((()))}"))

# define an empty list called stack
# define a dictionary pairs = { closer: opener }   # ) → (, ] → [, } → {

# for each char in the string s:

#     if char is an opener (in pairs values):
#         append char to stack

#     elif char is a closer (in pairs keys):
#         if stack is empty OR top of stack != matching opener (pairs[char]):
#             return False
#         else:
#             pop the top of stack

# after the loop:
#     return True if stack is empty, else False
