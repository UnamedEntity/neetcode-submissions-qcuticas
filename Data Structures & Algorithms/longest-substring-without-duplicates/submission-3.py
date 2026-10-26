class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        SetS = set()
        rightPointer = 0
        ans = 0
        for leftPointer in range(len(s)):
            while s[leftPointer] in SetS:
                SetS.remove(s[rightPointer])
                rightPointer += 1
            SetS.add(s[leftPointer])
            ans = max(ans, leftPointer - rightPointer + 1)
        return ans
            
        
        