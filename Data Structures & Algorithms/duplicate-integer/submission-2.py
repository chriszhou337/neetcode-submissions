from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        spotted = Counter(nums)

        for key, value in spotted.items():
            if value >= 2:
                return True

        return False