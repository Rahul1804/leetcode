def non_repeat_substring(s):
    if len(s) == 0:
        return 0
    window_start = 0
    max_len = 0
    my_map = {}

    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char in my_map:
            window_start = max(window_start, my_map[right_char]+1)

        my_map[right_char] = window_end

        max_len = max(max_len, window_end - window_start + 1)

    return max_len


def main():
    print("Length of the longest substring: " +
          str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abccde")))


main()
