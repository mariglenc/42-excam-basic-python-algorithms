#"""'''
#Write a function that creates a simple cipher by shifting letters in  a string by giving amount
#.Non alphabetic characters should not be changed.

#def whisper_cipher(text: str, shift: int) -> str:
#'''

#def whisper_cipher(text: str, shift: int) -> str:
#	result = ""
#	for char in text:
#		if ('a' <= char <= 'z'):
#			result += chr((ord(char) - ord('a')+ shift) % 26 + ord('a'))
#		elif ('A' <= char <= 'Z'):
#			result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
#		else:
#			result += char
#	return result

#print(whisper_cipher("abc", 1))

#def pattern_tracker(text: str) -> int:
#	count = 0

#	for i in range(len(text) - 1):
#		if text[i].isdigit and text[i + 1].isdigit:
#			if int(text[i + 1]) == int(text[i]) + 1 :
#				count += 1
#	return count

#print(pattern_tracker("123"))

#def string_sculptor(text : str) -> str:
#	result = ""
#	i_l = 0

#	for i, char in enumerate(text):
#		if char.isalpha():
#			if i_l % 2 == 0:
#				result += char.lower()
#			else:
#				result += char.upper()
#			i_l += 1
#		else:
#			result += char
#	return result


#print(string_sculptor("ab ab"))

#def pattern_tracker(text: str) -> int:
#	count = 0

#	for i in range(len(text) - 1):
#		if text[i].isdigit() and text[i + 1].isdigit():
#			if int(text[i + 1]) == int(text[i]) + 1:
#				count += 1
#	return count

#print(pattern_tracker("12a34"))

#def whisper_cipher(text: str, shift: int) -> str:
#	result = ""

#	for char in text:
#		if 'a' <= char <= 'z':
#			result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
#		elif 'A' <= char <= 'Z':
#			result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
#		else:
#			result += char
#	return result

#print(whisper_cipher("abc12", 1))


#def string_sculptor(text : str) -> str:
#	result =""
#	i_l = 0

#	for i, char in enumerate(text):
#		if char.isalpha():
#			if i_l % 2 == 0:
#				result += char.lower()
#			else:
#				result += char.upper()
#			i_l += 1
#		else:
#			result += char
#	return result

#print(string_sculptor("hh pp"))

#def mirror_matrix(matrix: list[list[int]]) -> list:
#	result = []

#	for row in matrix:
#		result.append(row[::-1])
#	return result

#print(mirror_matrix([[1, 2, 3, 3], [6, 7, 8], [1, 2 , 3]]))

#def cryptic_sort(strings: list[str]) -> list[str]:
#	return sorted(strings, key=lambda s: (len(s), s.lower(), sum(c in "aeuioAEUIO" for c in s)))

#print(cryptic_sort(["A", "banana", "grape", "kiwi", "oArange"]))


#def string_permutation_checker(str1: str, str2: str) -> bool:

#	str1 = str1.replace(" ", "").lower()
#	str2 = str2.replace(" ", "").lower()
#	return sorted(str1) == sorted(str2)

#print(string_permutation_checker("listen", "silent"))

#def twist_sequence(arr: list[int], k: int) -> list[int]:
#	if not arr:
#		return arr
#	k = k % len(arr)
#	return arr[-k:] + arr[:-k]

#print(twist_sequence([1, 2, 3 ,4 ,5], 2))

#def echo_validator(text: str) -> bool:
#	return text == text[::-1]

#print(echo_validator("heleh"))  # Output: True

#def pattern_tracker(text: str) -> int:
#	count = 0

#	for i in range(len(text) - 1):
#		if text[i].isdigit() and text[i + 1].isdigit():
#			if int(text[i + 1]) == int(text[i] + 1):
#				count += 1
#	return count

#print(pattern_tracker("01234567"))      # 7
#print(pattern_tracker("1234567890"))    # 8  
#print(pattern_tracker("987654321"))  # 0
#print(pattern_tracker("12a34"))  # 2


#def pattern_tracker(text: str) -> int:
#	count = 0

#	for i in range(len(text) - 1):
#		if text[i].isdigit() and text[i + 1].isdigit():
#			if int(text[i + 1]) == int(text[i]) + 1:
#				count += 1
#	return count

#print(pattern_tracker("01234567"))      # 7


#def twist_sequence(arr: list[int], k: int) -> list[int]:
#	if not arr:
#		return arr
#	k = k % len(arr)
#	return arr[-k:] + arr[:-k]

#print(twist_sequence([1, 2, 3, 4], 2))

#def string_sculptor(text : str) -> str:
#	result = ""
#	i_l = 0
#	for i, char in enumerate(text):
#		if char.isalpha():
#			if i_l % 2 == 0:
#				result += char.lower()
#			else:
#				result += char.upper()
#			i_l += 1
#		else:
#			result += char
		
#	return result

#print(string_sculptor("abc a"))


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
	digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	if (2 <= from_base <= 36 and 2 <= to_base 36):
		return "ERROR"
	try:
		num int(number, from_base)
	except:
			return "ERROR"
	
	if num == 0:
		return "0"
	result = ""
	while num > 0:
		result = digit[num % to_base] + result
		num //= to_base

	return result
