def ft_ulstr(s: str) -> str:
	result = ""
	for char in s:
		if 'a' <= char <= 'z':
			result += char.upper()
		elif 'A' <= char <= 'Z':
			result += char.lower()
		else:
			result += char
	return result

print(ft_ulstr("Hello, World!"))  # Output: "hELLO, wORLD!"