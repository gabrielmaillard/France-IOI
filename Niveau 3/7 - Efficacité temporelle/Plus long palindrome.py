def longest_palindrome_length(sequence):
    n = len(sequence)
    def expand_around_center(left, right):
        while left >= 0 and right < n and sequence[left] == sequence[right]:
            left -= 1
            right += 1
        return right - left - 1
    max_length = 0
    for i in range(n):
        length_odd = expand_around_center(i, i)
        length_even = expand_around_center(i, i + 1)
        current_max = max(length_odd, length_even)
        max_length = max(max_length, current_max)
    return max_length
sequence = input().strip()
print(longest_palindrome_length(sequence))