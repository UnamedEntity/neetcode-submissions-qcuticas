class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ls = defaultdict(int)
        lt = defaultdict(int)
        for i in range(len(s)):
            ls[s[i]] += 1
            lt[t[i]] += 1
        return ls == lt


        
        