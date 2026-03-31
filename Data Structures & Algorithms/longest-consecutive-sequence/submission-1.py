class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        dic = {}
        minNum = math.inf

        for n in nums:
            dic[n] = 0

        maxLen = 0

        for n in nums:
            i = 1
            localMax = 1
            while n + i in dic:
                localMax += 1
                i += 1
            maxLen = max(maxLen, localMax)
        
        return maxLen