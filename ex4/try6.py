# ex4 - cryptic_sort
# attempt: try6.py
# (signature pre-filled from the .en; write your solution below)
def count_vouels(word):
    count = 0
    vouels = "aeiouAEIOU"
    for char in word:
        if char in vouels:
            count += 1
    return count
 
def rank_values(word):
    word_len = len(word)
    word_lower = word.lower()
    word_vouel = count_vouels(word)
    return (word_len, word_lower, word_vouel)

def cryptic_sort(strings: list[str]) -> list:
    return sorted(strings,key=rank_values)
