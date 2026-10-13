class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      
        for i,v in enumerate(nums):
            val = target - v
            if val in nums[i+1:]: 
                return [i,nums.index(val,i+1)] # index(search_element, [start], [end])
        
        return 

        
        