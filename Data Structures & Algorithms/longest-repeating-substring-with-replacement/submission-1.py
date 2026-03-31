class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        res = 0
        l = 0
        for i in s:
            count[ord("A") - ord(i)] += 1
            if sum(count) - max(count) <= k:
                res = sum(count)
            else:
                count[ord("A") - ord(s[l])] -= 1
                l += 1
        return res
        