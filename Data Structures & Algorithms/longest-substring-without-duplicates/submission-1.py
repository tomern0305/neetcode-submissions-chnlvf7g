class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        res = 0
        count = 0

        while r < len(s):
            if s[r] not in seen:
                count += 1
                seen.add(s[r])
                r += 1

            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    count -= 1
                seen.add(s[r])
                r += 1
                count += 1
            
            res = max(count, res)

        return res
        