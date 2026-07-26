# ex4 - cryptic_sort
# attempt: try5.py
# (signature pre-filled from the .en; write your solution below)
def count_vouels(word):
    count = 0
    vouels = "aeiouAEIOU"
    for char in word:
        if char in vouels:
            count += 1
    return count

def ranking_values(word):
    word_count = len(word)
    word_lower = word.lower()
    word_vouel = count_vouels(word)
    return (word_count, word_lower, word_vouel)

def cryptic_sort(strings: list[str]) -> list:
    return sorted(strings, key=ranking_values)