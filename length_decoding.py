# Length decoding problem
# "a3b5g2a4n6" -> "aaabbbbbggaaaannnnnn"
# env: python3.8

s = "a1b2c3g1c2d3e4"
print(s)

decoded_s = ""
current_char = None
chars_group_len_str = None

for i in range(len(s)):
    char = s[i]

    if not char.isdigit():
        # first letter or letter from next chars group found,
        # need to save info about previous chars group
        if chars_group_len_str:
            chars_group_len = int(chars_group_len_str)
            decoded_s += current_char * chars_group_len

        # reset chars_group_len_str
        chars_group_len_str = None

        # override current_char by current one
        current_char = char
    else:
        # digit found
        if not chars_group_len_str:
            chars_group_len_str = char
        else:
            chars_group_len_str += char

    if i == len(s) - 1:
        # last char found
        chars_group_len = int(chars_group_len_str)
        decoded_s += current_char * chars_group_len


print(decoded_s)
