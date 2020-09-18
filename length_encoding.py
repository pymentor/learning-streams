# Length encoding problem
# aaabbccccdddaaaaaa -> a3b2c4d3a6
# env: python3.8

s = "aaabbccccdddaaaaaa"
print(s)

current_char = None
counter = None
string_chars_info = []

for i in range(len(s)):
    char = s[i]
    if char != current_char:
        # first char or new chars group
        if current_char:
            string_chars_info.append((current_char, counter))
        current_char = char
        counter = 1
    else:
        # next char in the same group
        counter += 1

    if i == len(s) - 1:
        # last char found
        string_chars_info.append((current_char, counter))

encoded_s = "".join(f"{el[0]}{el[1]}" for el in string_chars_info)
print(encoded_s)
