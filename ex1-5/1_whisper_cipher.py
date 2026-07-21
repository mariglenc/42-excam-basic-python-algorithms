
def whisper_cipher(text: str, shift: int) -> str:
	result = ""
	for char in text:
		if 'a' <= char <= 'z':
			result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
		elif 'A' <= char <= 'Z':
			result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
		else:
			result += char
	return result

print(whisper_cipher("Hello, World!", 3))  # Output: "Khoor, Zruog!"
print(whisper_cipher("Abz", 3))  # Output: "Dec"
print(whisper_cipher("WXYZ 1", 1))  # Output: "YZAB 1"