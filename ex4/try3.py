# ex4 - cryptic_sort
# attempt: try3.py
# (signature pre-filled from the .en; write your solution below)
def count_voules (word: str):
    count = 0
    voules = "aeiouAEIOU"
    for char in word:
        if char in voules:
            count += 1
    return count

def ranking_values(word: str):
    word_len = len(word)
    word_lower = word.lower()
    word_vouels = count_voules(word)
    return (word_len, word_lower, word_vouels)

def cryptic_sort(strings: list[str]) -> list:
    return sorted(strings, key=ranking_values)