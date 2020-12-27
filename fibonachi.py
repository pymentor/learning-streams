from functools import lru_cache

cache = {0: 1, 1: 1}


def fibo(n_):
    global cache

    if n_ not in cache:
        cache[n_] = fibo(n_ - 1) + fibo(n_ - 2)

    return cache[n_]


@lru_cache(maxsize=None)
def fibo1(n_):
    if n_ in (0, 1):
        return 1
    return fibo1(n_ - 1) + fibo1(n_ - 2)


def fibo2(n_):
    res = 1
    res_1 = 1
    res_2 = 1

    for i in range(n_ + 1):
        if i >= 2:
            res = res_1 + res_2
            res_1, res_2 = res, res_1

    return res


n = 400
print(fibo(n))
print(fibo1(n))
print(fibo2(n))
