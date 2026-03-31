class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) -1
        def water(l, r):
            return min(heights[l],heights[r])* (r - l)
        
        maxWater = water(l,r)
        
        while l < r:
            maxWater = max(water(l,r), maxWater)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxWater
