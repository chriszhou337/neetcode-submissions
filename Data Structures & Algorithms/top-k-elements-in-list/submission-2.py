class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for num in nums:
            my_map[num] = my_map.get(num, 0) + 1
        
        sorted_items = sorted(my_map.items(), key=lambda x: x[1], reverse=True)
        return [key for key, _ in sorted_items[:k]]

