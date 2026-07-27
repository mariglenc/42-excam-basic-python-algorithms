# ex1-1 - bracket_validator
# attempt: try13.py
# (signature pre-filled from the .en; write your solution below)

def bracket_validator(s: str) -> bool:
    openers = [] 
    pairs = {
        '}':'{',
        ']':'[',
        ')':'(',
    }
    for bracket in s:
        if bracket in pairs.values():
            openers.append(bracket)
        elif bracket in pairs.keys():
            if not openers or pairs[bracket] != openers[-1]:
                return False
            openers.pop()
            
    return len(openers) == 0
