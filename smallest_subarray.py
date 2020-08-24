import math


def smallest_sub_array_with_given_sum(s, arr):
    window_sum = 0
    min_length = math.inf
    window_start = 0

    for windows_end in range(0, len(arr)):
        window_sum += arr[windows_end]

        while window_sum >= s:
            min_length = min(min_length, windows_end-window_start+1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_length == math.inf:
        return 0

    return min_length


def main():
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
