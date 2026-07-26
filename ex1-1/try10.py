# ex1-1 - bracket_validator
# attempt: try10.py
# (signature pre-filled from the .en; write your solution below)

def bracket_validator(s: str) -> bool:
    openers = [] # declare a list for openers
    pairs = { # declare a fict with bracket pairs
        '}':'{',
        ')':'(',
        ']':'[',
    }
    for bracket in s:
        if bracket in pairs.values(): # check if bracket is opener
            openers.append(bracket) # append in opener list
        elif bracket in pairs.keys():
            if not openers or pairs[bracket] != openers[-1]:
                return False
            openers.pop()

    return len(openers) == 0