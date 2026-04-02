class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ana = {}
        for i in s:
            try:
                ana[i] += 1
            except:
                ana[i] = 1
        li = {}
        for x in t:
            try:
                li[x] += 1
            except:
                li[x] = 1
        return li == ana
            

        