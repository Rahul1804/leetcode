def remove_duplicates(arr):
    if len(arr) == 0:
        return -1

    next_non_duplicate = 1
    i = 1

    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate
