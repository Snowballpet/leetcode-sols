class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
      

        final = nums[0]
        result = abs(nums[0])
        for val in range(1,len(nums)):
            diff  = abs(nums[val])
            if diff < result or (diff == result and nums[val] > final):
                final = nums[val]
                result = diff 

        return final
        