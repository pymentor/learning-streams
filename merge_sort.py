def merge_sort(unsorted_array):
    # возращаем исходный список если он состоит из одного или менее элементов
    if len(unsorted_array) <= 1:
        return unsorted_array

    # находим средний индекс, чтобы начать рекурсивно делить пополам
    mid = len(unsorted_array) // 2

    # рекурсивно делим пополам
    left_part = unsorted_array[:mid]
    right_part = unsorted_array[mid:]

    left_part_req = merge_sort(left_part)
    right_part_req = merge_sort(right_part)

    # возврат результирующего отсортированного списка
    return merge(left_part_req, right_part_req)


def merge(left_list, right_list):
    sorted_list = []

    left_elem_index = right_elem_index = 0

    left_list_len = len(left_list)
    right_list_len = len(right_list)

    for _ in range(left_list_len + right_list_len):
        if left_elem_index < left_list_len and right_elem_index < right_list_len:
            # сравнение элементов каджого списка
            if left_list[left_elem_index] <= right_list[right_elem_index]:
                sorted_list.append(left_list[left_elem_index])
                left_elem_index += 1
            else:
                sorted_list.append(right_list[right_elem_index])
                right_elem_index += 1

        elif left_elem_index == left_list_len:
            # проверяем достигли ли конца левого списка
            sorted_list.append(right_list[right_elem_index])
            right_elem_index += 1

        elif right_elem_index == right_list_len:
            # проверяем достигли ли конца правого списка
            sorted_list.append(left_list[left_elem_index])
            left_elem_index += 1

    return sorted_list


print(merge_sort([1,4,2,3,1,5,1,5,8,2,4]))
