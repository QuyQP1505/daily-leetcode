class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        nums_length = len(sorted_nums)

        list_4sum = set()
        for i in range(nums_length-3):
            for j in range(i+1, nums_length-2):
                
                left = j + 1
                right = nums_length-1

                while left < right:
                    sum = sorted_nums[i] + sorted_nums[j] +  sorted_nums[left] + sorted_nums[right]
                    
                    if sum == target:
                        list_4sum.add((sorted_nums[i], sorted_nums[j], sorted_nums[left], sorted_nums[right]))
                        left += 1
                        right -= 1
                    elif sum > target:
                        right -= 1
                    else:
                        left += 1
        
        return list_4sum
                    
                
