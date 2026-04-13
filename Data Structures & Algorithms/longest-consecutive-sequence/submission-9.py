class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        start = []
        x = -1
        for i in nums:
            if i - 1 not in nums:
                start.append(i)
        count = [0]*len(start)
        for i in start:
            x += 1
            while i in nums:
                i += 1
                count[x] += 1
        return max(count)

        
        
            

            
        