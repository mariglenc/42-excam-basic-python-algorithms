
def string_permutation_checker(str1: str, str2: str) -> bool:
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

# Example usage:
print(string_permutation_checker("listen", "silent"))  # Output: True
print(string_permutation_checker("hello", "world"))    # Output: False
print(string_permutation_checker("Triangle", "Integral"))  # Output: True