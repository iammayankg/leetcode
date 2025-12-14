class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        N = len(words[0])
        def recurse(step, curr, results):
            if step == N:
                results.append(curr[:])
                return
            prefix = "".join(word[step] for word in curr)
            for word in words:
                if word.startswith(prefix):
                    curr.append(word)
                    recurse(step + 1, curr, results)
                    curr.pop()
        res = []
        recurse(0, [], res)
        return res
        