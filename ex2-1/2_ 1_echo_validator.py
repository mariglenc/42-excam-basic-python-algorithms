
def echo_validator(text: str) -> bool:
	cleaned = ""

	for char in text:
		if char.isalnum():
			cleaned += char.lower()
	return cleaned == cleaned[::-1]


print(echo_validator("hello"))  # Output: False
print(echo_validator("abc"))    # Output: False
print(echo_validator("ma dam"))  # Output: True
print(echo_validator("1 23 21"))  # Output: True
print(echo_validator("12345"))  # Output: False 