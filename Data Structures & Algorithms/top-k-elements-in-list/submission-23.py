class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dis = defaultdict(int)
        for i in nums:
            dis[i] += 1
        ans = []
        for y in range(0,k):
            big = 0
            val = 0
            for x in list(dis.keys()):
                if dis[x] > big:
                    big = dis[x]
                    val = x
            ans.append(val)
            dis[val] = 0
        return ans
        
                

