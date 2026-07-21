# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            median = (low + high) // 2

            if guess(median) == 0: #equal
                return median
            elif guess(median) == -1: # guessed median is too high
                high = median - 1
            elif guess(median) == 1: # guessed median is too low
                low = median + 1

        return 0