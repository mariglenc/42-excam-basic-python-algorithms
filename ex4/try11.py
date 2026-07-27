# ex4 - cryptic_sort
# attempt: try11.py
# (signature pre-filled from the .en; write your solution below)
def count_vowel(word):
    count = 0
    vouels = "aeiouAEIOU"
    for char in word:
        if char in vouels:
            count += 1
    return count


def rank_values(word):
    word_len = len(word)
    word_low = word.lower()
    word_vow = count_vowel(word)
    
    return (word_len, word_low, word_vow)


def cryptic_sort(strings: list[str]) -> list:
    return sorted(strings, key=rank_values)

