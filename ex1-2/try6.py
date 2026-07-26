# ex1-2 - number_base_converter
# attempt: try6.py
# (signature pre-filled from the .en; write your solution below)

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # decalre chars from 0 to z
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36): # validate bases from and to
        return "ERROR"
    try:
        nr = int(number,from_base) # convert number to int nr with int function insde try except
    except:
        return "ERROR"
    if nr == 0: # if nr is 0 return string 0
        return "0"

    value = ""
    while nr > 0:
        value = digits[nr % to_base] + value
        nr //= to_base

    return value
