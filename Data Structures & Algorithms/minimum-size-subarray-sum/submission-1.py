class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        L = 0
        minLen = len(nums) + 1
        currentSum = 0

        for R in range (len(nums)):
            currentSum += nums[R]

            while currentSum >= target:
                minLen = min(minLen, R - L + 1)
                currentSum -= nums[L]
                L += 1

        return 0 if minLen == len(nums) + 1 else minLen