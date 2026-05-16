#def string_sculptor(text : str) -> str:

#	result = ""
#	i_l = 0

#	for char in text:
#		if char.isalpha():
#			if i_l % 2 == 0:
#				result += char.lower()
#			else:
#				result += char.upper()
#			i_l += 1
#		else:
#			result += char
#	return result

#print(string_sculptor("ab 1c"))

#def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
#	merged = []
#	for i in range(max(len(list1), len(list2))):
#		if i < len(list1):
#			merged.append(list1[i])
#		if i < len(list2):
#			merged.append(list2[i])
#	return sorted(merged)


#def number_base_converter(number: str, from_base: int, to_base: int) -> str:
#		digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#		if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
#			return "ERROR"
		
#		try:
#			num = int(number, from_base)
#		except:
#			return "ERROR"
		
#		if num == 0:
#			return "0"
#		result = ""
#		while num > 0:
#			result = digits[num % to_base] + result
#			num //= to_base
#		return result


		

#print(number_base_converter("1010", 2, 10))  # Output: "10"

#def cryptic_sort(strings: list[str]) -> list:
#	return sorted(strings, key=lambda s: (len(s), s.lower(), sum(char in "aeuioAEUIO" for char in s)))


#def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
#	merged = []
#	for i in range(max(len(list1), len(list2))):
#		if i < len(list1):
#			merged.append(list1[i])
#		if i < len(list2):
#			merged.append(list2[i])
#	return merged





#print(shadow_merge([1, 2, 3], [4, 5, 6]))  # Output: [1, 4, 2, 5, 3, 6]
#print(shadow_merge([1, 2], [3, 4, 5, 5, 4, 3, 2, 1]))  # Output: [1, 3, 2, 4, 5, 5, 4, 3, 2, 1]

#def bracket_validator(s: str) -> bool:
#	stack = []
#	pairs = {')': '(', '}': '{', ']': '['}

#	for char in s:
#		if char in pairs.values():
#			stack.append(char)
#		elif char in pairs.keys():
#			if not stack or stack[-1] != pairs[char]:
#				return False
#			stack.pop()
#	return len(stack) == 0


#def pattern_tracker(text: str) -> int:
#	count = 0

#	for i in range(len(text) - 1):
#		if text[i].isdigit() == text [i + 1].isdigit():
#			if int(text[i + 1]) == int(text[i]) + 1:
#				count += 1
#	return count

#print(pattern_tracker("01234567"))      # 7
#print(pattern_tracker("1234567890"))    # 8  
#print(pattern_tracker("987654321"))  # 0
#print(pattern_tracker("12a34"))  # 2

