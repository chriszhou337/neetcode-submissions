class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1

        while index1 < index2:
            test = numbers[index1] + numbers[index2]

            if test == target:
                break
            elif test < target:
                index1+= 1
            elif test > target:
                index2-= 1

        return [index1 + 1, index2 + 1]