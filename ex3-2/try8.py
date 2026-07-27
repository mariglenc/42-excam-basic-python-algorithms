# ex3-2 - string_permutation_checker
# attempt: try8.py
# (signature pre-filled from the .en; write your solution below)

def string_permutation_checker(str1: str, str2: str) -> bool:
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)
