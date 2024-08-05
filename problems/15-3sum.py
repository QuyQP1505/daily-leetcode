from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                
                if sum3 == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif sum3 > 0:
                    right -= 1
                else:
                    left += 1
        
        return result
