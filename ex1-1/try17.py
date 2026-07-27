# ex1-1 - bracket_validator
# attempt: try17.py
# (signature pre-filled from the .en; write your solution below)

def bracket_validator(s: str) -> bool:
    openers = []
    pairs = {
        '}':'{',
        ']':'[',
        ')':'(',
    }
    for bra in s:
        if  bra in pairs.values():
            openers.append(bra)
        elif bra in pairs.keys():
            if not openers or pairs[bra] != openers[-1]:
                return False
            openers.pop()

    return len(openers) == 0
