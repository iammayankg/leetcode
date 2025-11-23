class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        w1 = len(word1)
        w2 = len(word2)

        if w1 < w2:
            word1, word2 = word2, word1
            w1, w2 = w2, w1

        @cache
        def dp(index1, index2):
            if index1 == w1 and index2 == w2:
                return 0
            if index1 == w1:
                return w2 - index2
            if index2 == w2:
                return w1 - index1
            next_cost = dp(index1+1, index2+1)
            if word1[index1] != word2[index2]:
                return 1 + min(dp(index1+ 1, index2), dp(index1, index2+1), next_cost)
            return next_cost

        return dp(0, 0)
        