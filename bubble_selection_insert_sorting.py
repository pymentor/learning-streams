from random import randint
from datetime import datetime
from time import time
from copy import copy


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        start1 = time()
        res = func(*args, **kwargs)
        duration = datetime.now() - start
        duration2 = time() - start1
        print(f"Elapsed time for {func.__name__}: {duration.microseconds} ms")
        print(f"Elapsed time for {func.__name__}: {duration2} s")
        return res
    return wrapper


@timer
def bubble_sort(haystack):
    switched = True
    while switched:
        switched = False
        for i in range(len(haystack) - 1):
            if haystack[i] > haystack[i+1]:
                switched = True
                haystack[i], haystack[i+1] = haystack[i+1], haystack[i]
    return haystack


@timer
def selection_sort(haystack):
    for i in range(len(haystack)):
        for j in range(i+1, len(haystack)):
            if haystack[j] < haystack[i]:
                haystack[j], haystack[i] = haystack[i], haystack[j]
    return haystack


@timer
def insert_sort(haystack):
    for i in range(1, len(haystack)):
        current = haystack[i]
        j = i - 1
        while j >= 0 and haystack[j] > current:
            haystack[j+1] = haystack[j]
            j -= 1
        haystack[j+1] = current
    return haystack


# O(n^2)
h1 = [randint(0, 10000) for _ in range(1000)]
h2 = copy(h1)
h3 = copy(h1)

print(h1)
print(bubble_sort(h1))

print(h2)
print(selection_sort(h2))

print(h3)
print(insert_sort(h3))
