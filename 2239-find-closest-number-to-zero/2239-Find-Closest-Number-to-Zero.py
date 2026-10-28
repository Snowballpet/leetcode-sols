class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
      

        final = nums[0]
        abs_val = abs(nums[0])
        for val in nums:
            diff = abs(val)
            if diff < abs_val or (diff == abs_val and val > final):
                final = val
                abs_val = diff

        return final
        