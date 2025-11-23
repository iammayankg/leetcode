class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def counts(num):
            c = Counter()
            while num:
                c[num%10] += 1
                num = num // 10
            return c
        
        def isBalanced(c):
            for num, count in c.items():
                if num != count:
                    return False
            return True
        n += 1
        while True:
            if isBalanced(counts(n)):
                return n
            n += 1
        return n