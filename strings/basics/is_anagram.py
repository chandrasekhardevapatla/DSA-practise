def is_anagram(string1: str, string2: str) -> bool:
    """
    Determines both strings are anagrams or not

    Anagram: If character count in both strings are equal then both strings are anagrams
    """

    string1_char_count, string2_char_count = {}, {}
    for char in string1:
        if char in string1_char_count:
            string1_char_count[char] += 1
        else:
            string1_char_count[char] = 1

    for char in string2:
        if char in string2_char_count:
            string2_char_count[char] += 1
        else:
            string2_char_count[char] = 1
    
    for char, char_count in string1_char_count.items():
        if char in string2_char_count:
            if string2_char_count[char] == char_count:
                del string2_char_count[char]
        else:
            return False
    if len(string2_char_count) > 0:
        return False
    return True
