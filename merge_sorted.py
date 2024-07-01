# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
# Merge sorted arrays

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        last_elem = m + n - 1

        while i > 0 or j >= 0:
            if i >= 0:
                if j >= 0:
                    if nums1[i] < nums2[j]:
                        nums1[last_elem] = nums2[j]
                        j -= 1
                    else:
                        nums1[last_elem] = nums1[i]
                        i -= 1
                else:
                    nums1[last_elem] = nums1[i]
                    i -= 1
            else:
                nums1[last_elem] = nums2[j]
                j -= 1
            last_elem -=1

