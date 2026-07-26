# ex1-1 - bracket_validator
# attempt: try11.py
# (signature pre-filled from the .en; write your solution below)

def bracket_validator(s: str) -> bool:
    openers = [] # declare a list for opener brackets
    pairs = { # declare bracket pairs dict for openers and closers
        '}':'{',
        ']':'[',
        ')':'(',
    }
    for bracket in s:
        if bracket in pairs.values(): # check if is opner
            openers.append(bracket) # append in openrs list
        elif bracket in pairs.keys(): # check if closer
            if not openers or pairs[bracket] != openers[-1]:
                return False
            openers.pop()
    return len(openers) == 0
 
