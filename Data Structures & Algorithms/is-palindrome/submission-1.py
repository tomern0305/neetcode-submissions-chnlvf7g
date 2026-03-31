class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""

        for i in s:
            if i.isalpha() or i.isnumeric():
                newS += i.lower()

        return newS == newS[::-1]