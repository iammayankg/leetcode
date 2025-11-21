class Solution:
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        def recurse(left, right, count):
            res = True
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1
            if left >= right:
                return res
            if count > 0:
                return recurse(left+1, right, count-1) or recurse(left, right-1, count-1)
            else:
                return False
        return recurse(0, N-1, 1)
        