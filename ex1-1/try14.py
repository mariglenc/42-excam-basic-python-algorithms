# ex1-1 - bracket_validator
# attempt: try14.py
# (signature pre-filled from the .en; write your solution below)

def bracket_validator(s: str) -> bool:
    openers = [] # declare a list for opener brackets
    pairs = { # declare a dict with all pairs of bracket closer openers
        '}':'{',
        ']':'[',
        ')':'(',
    }
    for bracket in s:
        if bracket in pairs.values(): # check if bracket is opener
            openers.append(bracket) # append it to the openers list
        elif bracket in pairs.keys(): # check if bracket is closer
            if not openers or pairs[bracket] != openers[-1]:
                return False
            openers.pop()

    return len(openers) == 0

