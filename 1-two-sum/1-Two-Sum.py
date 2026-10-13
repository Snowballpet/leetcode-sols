class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapping ={}
        for i,v in enumerate(nums):
            val = target - v
            if val in mapping:
                return [mapping[val], i]
            mapping[v] = i

        return 

        
        