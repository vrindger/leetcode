import copy
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        merged_nums = []
        count = 0
        for count in range(m+n+1):
            print(i, j, count, merged_nums)
            if i < m:
                if j < n:
                    if nums1[i] <= nums2[j]:
                        merged_nums.append(nums1[i])
                        i+=1
                    else:
                        merged_nums.append(nums2[j])
                        j+=1
                else:
                    merged_nums.append(nums1[i])
                    i+=1
            else:
                if j < n:
                    merged_nums.append(nums2[j])
                    j+=1
        nums1=[]
        for i in merged_nums:
            nums1.append(i)
        print(nums1)