# ex1-2 - number_base_converter
# attempt: try10.py
# (signature pre-filled from the .en; write your solution below)

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # declare all digits
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36): # validate bases
        return "ERROR"
    try: 
        nr = int(number,from_base) # convert from base number to int nr
    except:
        return "ERROR"
    if nr == 0:
        return "0"
    value = ""
    while nr > 0:
        value = digits[nr % to_base] + value
        nr //= to_base
    return value