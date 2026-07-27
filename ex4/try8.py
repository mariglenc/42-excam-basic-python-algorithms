# ex4 - cryptic_sort
# attempt: try8.py
# (signature pre-filled from the .en; write your solution below)
def count_vowels(word):
    count = 0
    vouels = "aeiouAEIOU"
    for char in word:
        if char in vouels:
            count += 1
    return count


def rank_values(word):
    word_len = len(word)
    word_lower = word.lower()
    word_vowels = count_vowels(word)
    
    return (word_len, word_lower, word_vowels)
    

def cryptic_sort(strings: list[str]) -> list:
    return sorted(strings, key=rank_values)
