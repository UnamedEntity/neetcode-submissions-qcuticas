class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for x in range(1,len(nums)):
                if nums[x] + nums[i] == target:
                    if x != i:
                        return [i,x]
        
        