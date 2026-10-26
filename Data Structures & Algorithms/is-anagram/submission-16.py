class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        listS = defaultdict(int)
        listT = defaultdict(int)
        for i in range(len(s)):
            listS[s[i]] += 1
            listT[t[i]] += 1
        return listS == listT
        