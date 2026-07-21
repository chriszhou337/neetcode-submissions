class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()

        for num in nums:
            numsSet.add(num)

        maxLen = 0

        for i in range (len(nums)):
            testNum = nums[i]
            testLen = 1

            while testNum + 1 in numsSet:
                testLen+=1
                testNum+=1
            
            maxLen = max(testLen, maxLen)

        return maxLen




