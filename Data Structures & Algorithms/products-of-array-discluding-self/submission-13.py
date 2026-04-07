class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 0:
            return nums
        ans = [1] 
        prefix = 1
        for i in range(len(nums)-1):
            ans.append(nums[i]*prefix)
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i]*postfix
            postfix *= nums[i] 
        return ans
        

        

        