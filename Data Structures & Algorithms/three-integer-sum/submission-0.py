class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []

        nums.sort()
        print(nums)

        for L in range (len(nums) - 2):
            if L != 0 and nums[L] == nums[L - 1]:
                continue
        
            target = -1 * nums[L]

            left = L + 1
            right = len(nums) - 1
            
            while left < right:
                sum = nums[left] + nums[right]

                if sum == target:
                    arr = [nums[L], nums[left], nums[right]]
                    solution.append(arr)

                    while left < right and nums[left] == nums[left + 1]:
                        left +=1
                    while left < right and nums[right] == nums[right - 1]:
                        right -=1
                    left +=1
                    right -=1
                elif sum < target:
                    left +=1
                elif sum > target:
                    right -=1

        return solution