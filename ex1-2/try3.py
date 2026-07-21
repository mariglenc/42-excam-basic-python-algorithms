
def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # DECLARE DIGITS

    if not (2 <= from_base <= 36 and 2 <= to_base <= 36): # validate the bases are inside 2 and 36
        return "ERROR" # if not return error
    
    try: # with try except convert number with int func and from base param to int
        num = int(number,from_base)
    except: # if fails return error
        return "ERROR" 
    
    if num == 0: # if num is 0 return 0
        return "0"
    
    result = ""
    while num > 0:
        result = digits[num%to_base]+result # add here each digit
        num = num // to_base # go to the next digit
    
    return result


print(number_base_converter("1010", 2, 10))  # Output: "10"
print(number_base_converter("1A", 16, 10))    # Output: "26"
print(number_base_converter("Z", 36, 10))     # Output: "35"
print(number_base_converter("123", 10, 2))    # Output: "1111011"
print(number_base_converter("123", 10, 37))   # Output: "ERROR"
print(number_base_converter("1G", 16, 10))    # Output: "ERROR"
print(number_base_converter("1A", 10, 16))    # Output: "ERROR"