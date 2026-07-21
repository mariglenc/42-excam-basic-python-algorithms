def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    # 1: decare digits
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # 2: validate bases - bases must be bigger than 2 and smalelr than 36
    if not (2 <= to_base <= 36 and 2 <= from_base <= 36):
        return "ERROR"

    # convert input to int base 2 with try excecpt
    try:
        num = int(number, from_base)
    except:
        return "ERROR"

    # if num is 0 return 0
    if num == 0:
        return "0"

    result = ""
    while num > 0:
        result = digits[num % to_base] + result
        num = num // to_base
    
    return result


print(number_base_converter("1A", 16, 10))    # Output: "26"
print(number_base_converter("Z", 36, 10))     # Output: "35"
print(number_base_converter("123", 10, 2))    # Output: "1111011"
print(number_base_converter("123", 10, 37))   # Output: "ERROR"
print(number_base_converter("1G", 16, 10))    # Output: "ERROR"
print(number_base_converter("1A", 10, 16))    # Output: "ERROR"