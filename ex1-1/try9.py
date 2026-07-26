# ex1-1 - bracket_validator
# attempt: try9.py
# (signature pre-filled from the .en; write your solution below)

def bracket_validator(s: str) -> bool:
    openers = []
    pairs = {
        '}':'{',
        ')':'(',
        ']':'[',
    }
    for bracket in s: # iterate over all brackets of s
        if bracket in pairs.values(): # check if is opener
            openers.append(bracket) # append to openers
        elif bracket in pairs.keys(): # check if is closer
            if not openers or pairs[bracket] != openers[-1]:
                return False
            openers.pop()

    return len(openers) == 0
