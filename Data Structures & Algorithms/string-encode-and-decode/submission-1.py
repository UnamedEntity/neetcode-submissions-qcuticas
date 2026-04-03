class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += i + '¥'
        return ans


    def decode(self, s: str) -> List[str]:
        ans = []
        strs = ""
        for i in s:
            if i == '¥':
                ans.append(strs)
                strs = ""
            else:
                strs += i
        return ans


