class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        found = False
        length = len(nums)
        for i in range(0, length+1):
            found = False
            for j in nums:
                if i == j:
                    found = True
            if found == False:
                return i
        return 0