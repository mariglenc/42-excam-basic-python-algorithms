# count vowels
def count_vowels(word:str):
    counter = 0
    vouels = "aeiouAEIOU"
    for char in word:
        if char in vouels:
            counter += 1
    return counter

# rankin values
def ranking_values(word: str):
    word_len = len(word)
    word_lower = word.lower()
    vouels = count_vowels(word)

    # return (lenght, word in lower, vouels)
    return (word_len, word_lower, vouels)

# main function pass ranking values at key
def cryptic_sort(strings: list[str]) -> list:
    return sorted(strings, key=ranking_values)

print(cryptic_sort(["zxcas", "asdasdas", "A", "as", "asd"]))  # ['A', 'kiwi', 'grape', 'banana', 'oArange']  (pure length: 1,4,5,6,7)
print(cryptic_sort(["A", "banana", "grape", "kiwi", "oArange"]))  # ['A', 'kiwi', 'grape', 'banana', 'oArange']  (pure length: 1,4,5,6,7)
print(cryptic_sort(["a", "e", "b", "o", "u"]))                    # ['a', 'b', 'e', 'o', 'u']  (all length 1, so alphabetical)
print(cryptic_sort(["Mariglen", "mariglen", "MARIGLEN"]))         # ['Mariglen', 'mariglen', 'MARIGLEN']  (all tie on every rule -> original order kept)
print(cryptic_sort(["aaa", "AAA", "bbb", "BBB"]))                 # ['aaa', 'AAA', 'bbb', 'BBB']  (a's before b's; case ties keep original order)