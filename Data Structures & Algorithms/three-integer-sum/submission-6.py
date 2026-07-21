class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []

        for i in range (len(nums) - 2):
            L = i + 1
            R = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while L < R:

                sumTest = nums[i] + nums[L] + nums[R]

                if sumTest < 0:
                    L += 1
                elif sumTest > 0:
                    R -= 1
                else:
                    solution.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        return solution
