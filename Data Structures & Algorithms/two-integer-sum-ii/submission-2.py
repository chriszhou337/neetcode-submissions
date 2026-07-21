class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            test = numbers[R] + numbers[L]

            if test == target:
                print("Done")
                return [L + 1, R + 1]
            elif test < target:
                print("Too small")
                L += 1
            else:
                print("Too big")
                R -= 1

        return 0