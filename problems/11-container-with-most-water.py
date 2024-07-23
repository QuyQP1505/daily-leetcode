from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest_capacity = 0
        right = len(height) - 1
        left = 0
        
        while left < right:
            current_capacity = min(height[left], height[right]) * (right - left)
            largest_capacity = max(largest_capacity, current_capacity)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return largest_capacity