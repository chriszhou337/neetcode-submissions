class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(heights) - 1
        maxArea = 0

        while left_ptr < right_ptr:
            area = (right_ptr - left_ptr) * min(heights[left_ptr], heights[right_ptr])
            maxArea = max(maxArea, area)

            if heights[left_ptr] < heights[right_ptr]:
                left_ptr+=1
            else:
                right_ptr-=1

        return maxArea