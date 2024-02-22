class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        binaryList = list()
        counter = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            counter += 1
        return right << counter