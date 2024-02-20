class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i]+nums[j] == target and i != j:
                    returnList = [i, j]
                    return returnList