# count voules
def count_voules(word: str):
    count = 0
    voules = "aeiouAEIOU"
    for char in word:
        if char in voules:
            count +=1
    return count


# ranking_values
def ranking_values(word: str):
    word_len = len(word)
    word_lower = word.lower()
    word_vouel = count_voules(word)
    return (word_len, word_lower, word_vouel)

def cryptic_sort(strings: list[str]) -> list:
    return sorted(strings, key=ranking_values)

print(cryptic_sort(["A", "banana", "grape", "kiwi", "oArange"]))  # ['A', 'kiwi', 'grape', 'banana', 'oArange']  (pure length: 1,4,5,6,7)
print(cryptic_sort(["a", "e", "b", "o", "u"]))                    # ['a', 'b', 'e', 'o', 'u']  (all length 1, so alphabetical)
print(cryptic_sort(["Mariglen", "mariglen", "MARIGLEN"]))         # ['Mariglen', 'mariglen', 'MARIGLEN']  (all tie on every rule -> original order kept)
print(cryptic_sort(["aaa", "AAA", "bbb", "BBB"]))                 # ['aaa', 'AAA', 'bbb', 'BBB']  (a's before b's; case ties keep original order)
