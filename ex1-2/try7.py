# ex1-2 - number_base_converter
# attempt: try7.py
# (signature pre-filled from the .en; write your solution below)

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # decalre digits 0 to Z
    if not (0 <= from_base <= 36 and 0 <= to_base <= 36 ): # validate bases length
        return "ERROR"
    try:
        nr = int(number, from_base)
    except:
        return "ERROR"
    if nr == 0: # if nr is 0 return string 0
        return "0"
    values = ""
    while nr > 0:
        values = digits[nr % to_base] + values
        nr //= to_base

    return values
