# ex1-5 - whisper_cipher
# attempt: try5.py
# (signature pre-filled from the .en; write your solution below)

def whisper_cipher(text: str, shift: int) -> str:
    shifted = ""
    for char in text:
        if 'a' <= char <= 'z': 
            shifted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z': 
            shifted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            shifted += char

    return shifted

print(whisper_cipher("abc", 1))            # -> "bcd"
print(whisper_cipher("xyz", 3))           # -> "abc"
print(whisper_cipher("Hello, World!", 13)) # -> "Uryyb, Jbeyq!"
print(whisper_cipher("ABC", -1))           # -> "ZAB"
