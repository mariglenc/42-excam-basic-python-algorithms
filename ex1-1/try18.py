# ex1-1 - bracket_validator
# attempt: try18.py
# (signature pre-filled from the .en; write your solution below)

def bracket_validator(s: str) -> bool:
    openers = []
    pairs = {
        '}': '{',
        ']': '[',
        ')': '(',
    }
    for brc in s:
        if brc in pairs.values():
            openers.append(brc)
        elif brc in pairs.keys():
            if not openers or pairs[brc] != openers[-1]:
                return False
            openers.pop()
    
    return len(openers) == 0
