from string import ascii_letters
from random import randint


"""
LINEAR SEARCH
"""


def linear_search(s_, sub_s_):
    sub_s_first_char = sub_s_[0]
    sub_s_len = len(sub_s_)

    for i in range(len(s_)):
        curr_char = s_[i]
        if curr_char == sub_s_first_char:
            s_slice = s_[i:i+sub_s_len]
            if sub_s_ == s_slice:
                return i


s = "".join([ascii_letters[randint(1, len(ascii_letters) - 1)] for _ in range(100000)])
print(f"Haystack: {s}")

sub_s = "kNe"
print(f"Needle: {sub_s}")

res = linear_search(s, sub_s)
print(f"Result: {'found: ' + str(res) if res else 'not found'}. ")


"""
BINARY SEARCH
"""

sorted_array = list(filter(lambda x: ((x // 3) + (x // 5)) % 7 == 0, range(1000)))
print(sorted_array)


# we don't need cache here

def binary_search(haystack, needle):
    """
    recursion function
    """
    middle_index = len(haystack) // 2

    if haystack[middle_index] == needle:
        return True

    if len(haystack) == 1 and haystack[0] != needle:
        return False

    if needle < haystack[middle_index]:
        return binary_search(haystack[:middle_index], needle)

    if needle > haystack[middle_index]:
        return binary_search(haystack[middle_index:], needle)


def binary_search2(haystack, needle):
    """
    function w/o recursion
    """

    if needle > haystack[-1] or needle < haystack[0]:
        return False

    min_index = 0
    max_index = len(haystack) - 1

    while max_index >= min_index:
        middle_index = (max_index + min_index) // 2
        if haystack[middle_index] == needle:
            return True
        if haystack[middle_index] < needle:
            min_index = middle_index + 1
            continue
        if haystack[middle_index] > needle:
            max_index = middle_index - 1
            continue


n = 40
print(n)

res = binary_search(sorted_array, n)
print(f"Result: {'found' if res else 'not found'}")

res = binary_search2(sorted_array, n)
print(f"Result: {'found' if res else 'not found'}")
