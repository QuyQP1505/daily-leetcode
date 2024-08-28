class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_list = []

        for num in nums:
            if num not in unique_list:
                unique_list.append(num)

        nums[:] = unique_list
        return len(unique_list)