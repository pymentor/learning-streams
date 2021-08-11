# Length encoding problem
# aaabbccccdddaaaaaa -> a3b2c4d3a6
# env: python3.8

s = "aaabbccccdddaaaaaa"
print(s)

current_char = None
counter = None
encodes_s = ""

len_s = len(s)

for i in range(len_s):
    char = s[i]
    if char != current_char:
        # first char or new chars group
        if current_char:
            encodes_s += f"{current_char}{counter}"
        current_char = char
        counter = 1
    else:
        # next char in the same group
        counter += 1

    if i == len_s - 1:
        # last char found
        encodes_s += f"{current_char}{counter}"

print(encodes_s)
