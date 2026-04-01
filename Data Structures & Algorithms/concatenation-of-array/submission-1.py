class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = list(nums) + list(nums)
        # for n in nums:
        #     ans.append(n)
        return ans
