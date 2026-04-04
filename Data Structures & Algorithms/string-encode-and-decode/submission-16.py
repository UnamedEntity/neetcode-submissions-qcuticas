class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        if len(strs) == 0:
            return ""
        for i in strs:
            ans += i + '¥'    
        return ans


    def decode(self, s: str) -> List[str]:
        ans = []
        if len(s) == 0:
            return []
        elif s[-1] == '¥':
            s = s[:-1]
        ans = s.strip().split('¥')
        return ans


