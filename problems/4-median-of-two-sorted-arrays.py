from typing import List
from math import floor

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = nums1 + nums2
        sorted_arr = sorted(new_arr)

        med_idx = floor(len(sorted_arr)//2)

        if len(sorted_arr) % 2 == 0:
            median_val_1 = sorted_arr[med_idx-1]
            median_val_2 = sorted_arr[med_idx]

            result = (median_val_1 + median_val_2) / 2
        else:
            result = sorted_arr[med_idx]

        return result 