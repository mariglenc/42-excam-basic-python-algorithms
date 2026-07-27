# ex1-2 - number_base_converter
# attempt: try13.py
# (signature pre-filled from the .en; write your solution below)

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # declare all digits
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36): # validate bases length
        return "ERROR"
    try: # convert number to int nr from base int with try except
        nr = int(number,from_base)
    except:
        return "ERROR"
    if nr == 0: # if nr int 0 return string 0
        return "0"
    converted = "" # declare a empty string FOR number
    while nr > 0: 
        converted = digits[nr%to_base] + converted
        nr //=to_base
    return converted
