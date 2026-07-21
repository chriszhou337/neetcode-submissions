class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        spotted = set()

        for i in nums:
            if i in spotted:
                return True
            else:
                spotted.add(i)

        return False