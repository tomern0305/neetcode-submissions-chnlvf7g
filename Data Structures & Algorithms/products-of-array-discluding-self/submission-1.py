class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1

        for i in range(n):
            res[i] = nums[i] * prefix
            prefix = res[i]
        
        sufix = 1

        for i in range(n-1, -1, -1):
            if i > 0:
                res[i] = res[i -1] * sufix
            else:
                res[i] = sufix
                
            sufix *= nums[i]

        return res

        