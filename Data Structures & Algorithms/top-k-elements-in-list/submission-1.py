class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        res = []

        for i in range(k):
            res.append(max(dic, key=dic.get))
            dic.pop(res[i])

        return res