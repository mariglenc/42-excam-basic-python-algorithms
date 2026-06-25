def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"
    try:
        number = int(number, from_base)
    except:
        return "ERROR"
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        result = digits[number % to_base] + result
        number = number // to_base
    return result
