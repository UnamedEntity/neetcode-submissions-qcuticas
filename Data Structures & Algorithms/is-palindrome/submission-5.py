class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return false
        start = 0
        s = s.replace(" ","")
        end = len(s)-1
        symbols = ":;.,?'!"
        while start < end:
            if s[end] in symbols:
                end -= 1
            elif s[start] in symbols:
                start += 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True
        