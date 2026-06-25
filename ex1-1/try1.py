
def bracket_validator(s: str) -> bool:
    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


result = bracket_validator("[(]")
print("result is:", result)

# declare stack: type list - []
# declare pairs: type dictionary - {key:value}
# iterate over string
# check if itereted value is in pairs value -> if it is append to stack
# else if iterated value is in pairs key ->
#   if stack is empty or last value of stack != value of dict[value]
#       return FALSE
#   stack pop() -> removes last value
# return len of stack == 0
