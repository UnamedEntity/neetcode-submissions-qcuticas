class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)
        for i in strs:
            ls = [0]*26
            for x in i:
                ls[ord(x)-ord('a')] += 1
            ans[tuple(ls)].append(i)
        return list(ans.values())


            
