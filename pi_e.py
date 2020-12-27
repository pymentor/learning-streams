from math import pi, e

# Формула Лейбница
# pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ....
#
#       n   4*(-1)^i
# pi = SUM -----------, i = (0,1,2,...)
#       i=0   2*i+1


def _pi(n):
    res = 0.0
    for i in range(n+1):
        res += (4 * (-1)**i) / (2*i + 1)
    return res


print(pi)
print(_pi(10000000))


# Ряд Тейлора
#      n    (1)^i
# e = SUM -----------, i = (0,1,2,3,...)
#     i=0     i!


def factorial(k):
    res = 1
    for i in range(1, k+1):
        res *= i
    return res


def exp(n):
    res = 0.0
    for i in range(n+1):
        res += (1**i) / factorial(i)
    return res


print(e)
print(exp(20))
