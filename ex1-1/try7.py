# ex1-1 - bracket_validator
# attempt: try7.py
# (signature pre-filled from the .en; write your solution below)

def bracket_validator(s: str) -> bool:
    openers = [] # decalre an empty list just for openers
    pairs = { # decalre all pairs closers and openers
        '}':'{',
        ')':'(',
        ']':'['
    }
    for bracket in s:
        if bracket in pairs.values(): # if it is opener append to openers
            openers.append(bracket)
        elif bracket in pairs.keys(): # if it is closer
            # chek if the openers is empt or the inner bracket does not match with current bracket on iteration
            if not openers or pairs[bracket] != openers[-1]: 
                return False
            openers.pop()

    return len(openers) == 0
