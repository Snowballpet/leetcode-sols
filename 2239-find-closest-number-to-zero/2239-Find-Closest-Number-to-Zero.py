class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
      

        final = nums[0]
        for val in nums:
            if abs(val) < abs(final) or (abs(val) == abs(final) and val > final):
                final = val

        return final
        