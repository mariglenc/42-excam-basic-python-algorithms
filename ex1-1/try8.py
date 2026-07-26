# ex1-1 - bracket_validator
# attempt: try8.py
# (signature pre-filled from the .en; write your solution below)

def bracket_validator(s: str) -> bool:
    openers = [] # declare empty list of openers
    pairs = { # declare a dictionary of brackets closers openers
        '}':'{',
        ')':'(',
        ']':'[',
    }
    for bracket in s:
        if bracket in pairs.values(): # check if opener
            openers.append(bracket) # append to openers list
        elif bracket in pairs.keys():
            if not openers or pairs[bracket] != openers[-1]:
                return False
            openers.pop()

    return len(openers) == 0