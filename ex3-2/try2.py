def string_permutation_checker(str1: str, str2: str) -> bool:
    # remove the spaces of string 1 and make lowercase
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    # sort all chars of boths string and check if the same
    # if so it means they anagrams and return true
    return sorted(str1) == sorted(str2)
