class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        remain_list = []

        for num in nums:
            if num != val:
                remain_list.append(num)

        nums[:] = remain_list
        return len(remain_list)