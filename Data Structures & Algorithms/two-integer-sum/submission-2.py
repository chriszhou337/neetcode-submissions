class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i in range (len(nums)):
            indexes[nums[i]] = i
        
        print(indexes)
        
        solution = []
        for i in range (len(nums)):
            lookup = target - nums[i]
            print(lookup)
            if lookup in indexes and indexes[lookup] != i:
                solution.append(i)
                solution.append(indexes[lookup])
                solution.sort()
                return solution

        