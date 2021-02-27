"""

Пусть S(n) = 1 + 2 + ... + n, например S(4) = 1 + 2 + 3 + 4 = 10

Необходимо по заданному n найти количество нулей, на которые оканчивается число S(n)

"""

def get_sum(n):
    s = 0

    for num in range(1, n + 1):
        s += num

    return s


def get_zeros_number(n):
    if n == 0:
        return 1

    divider = 10
    zeros_number = 0

    while n % divider == 0:
        zeros_number += 1
        divider *= 10

    return zeros_number


for i in range(10000):
    s = get_sum(i)
    zn = get_zeros_number(s)
    if zn != 0:
        print(f"Number: {i}, S(n): {s}, Zeros number: {zn}")
