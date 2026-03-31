class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_num = []
        for i in nums:
            if i in new_num:
                return True
            new_num.append(i)
        return False
            
            
        