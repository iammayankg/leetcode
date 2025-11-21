class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_digits(k):
            s = 0
            while k:
                d = k % 10
                s += d*d
                k = k//10
            return s
        curr = sum_digits(n)
        if curr == 1:
            return True
        seen = set()
        while curr not in seen:
            seen.add(curr)
            curr = sum_digits(curr)
            if curr == 1:
                return True
        return False

        