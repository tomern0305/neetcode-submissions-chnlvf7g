class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forw = [0]*len(nums)
        back = [0]*len(nums)

        for i,num in enumerate(nums):
            if i > 0:
                forw[i] = forw[i - 1] * num
            else:
                forw[i] = num

        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                back[i] = back[i + 1] * nums[i]
            else:
                back[i] = nums[i]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i > 0 and i < len(nums) - 1:
                res[i] = forw[i-1] * back[i+1]
            elif i == 0:
                res[i] = back[i+1]
            elif i == len(nums) - 1:
                res[i] = forw[i-1]
        
        return res
        