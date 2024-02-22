class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        for i in nums2:
            nums1.append(i)
        
        nums1.sort()

        length = len(nums1)

        if length % 2 == 1:
            value = nums1[int(length/2)]
            return float(value)

        else:
            value = (nums1[int((length/2)-1)]+nums1[int(length/2)])/2
            return float(value)