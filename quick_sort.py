def quick_sort(unsorted_list):
    def _helper(array, low_index, high_index):
        if low_index < high_index:
            split_index = partition(array, low_index, high_index)
            _helper(array, low_index, split_index)
            _helper(array, split_index + 1, high_index)

    _helper(unsorted_list, 0, len(unsorted_list) - 1)


def partition(array_list, low, high):
    middle_index = (low + high) // 2
    middle_elem = array_list[middle_index]

    i = low - 1
    j = high + 1

    while True:
        i += 1
        while array_list[i] < middle_elem:
            i += 1

        j -= 1
        while array_list[j] > middle_elem:
            j -= 1

        if i >= j:
            return j

        array_list[i], array_list[j] = array_list[j], array_list[i]


arr = [1,4,2,3,1,5,1,5,8,2,4]
quick_sort(arr)
print(arr)
