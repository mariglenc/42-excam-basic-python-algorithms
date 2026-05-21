def bracket_validator(s: str) -> bool:
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    print("executed")

    for char in s:

        # checks whether the current character is an opening bracket.
        if char in pairs.values():
            stack.append(char)

        # Check if the character is a closing bracket
        elif char in pairs.keys():

            # checks if the stack is empty

            # OR stack = [ "[", "]" ]

            # if the latest opening bracket does not match
            if not stack or stack[-1] != pairs[char]:
                print("exit point returned false")
                return False

            # removes the matched opening bracket
            stack.pop()

    # returns True if all brackets were matched
    return len(stack) == 0


# bracket_validator("asd[")
# bracket_validator("()[]{}")   # True
# bracket_validator("([{}])")   # True
bracket_validator("[])")       # False
# bracket_validator("([)]")     # False
# bracket_validator("")         # True
