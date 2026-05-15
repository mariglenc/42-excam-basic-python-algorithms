def cryptic_sort(strings: list[str]) -> list:
    return sorted(
        strings,
        key=lambda s: (len(s), s.lower(), sum(char in 'aeiouAEIOU' for char in s))
    )
