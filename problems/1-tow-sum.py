from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} 
        for idx, val in enumerate(nums):
            remain = target - val
            if remain in d:
                return [d[remain], idx]
            d[val] = idx