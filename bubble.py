def bubble_k(array):
    last = len(array)-1
    i = 0
    k = 0

    while True:
        if array[last-i] < array[last-1-i]:
            array[last-i], array[last-1-i] = array[last-1-i], array[last-i]
            i += 1
        else:
            i += 1
        if i == last:
            i = 0
            k += 1
        if k == last:
            break
    return array


the_list = [5, 6, 1, 9, 6, 7, 3, 9, 8, 5, 1, 2, 1, 3, 5, 6, 5, 1, 2, 9, 5, 9]
print(bubble_k(the_list))

