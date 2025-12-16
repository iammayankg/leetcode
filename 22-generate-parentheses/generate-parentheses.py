class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtrack(curr, left, right):
            if len(curr) == 2*n:
                answer.append("".join(curr))
                return

            if left < n:
                curr.append("(")
                backtrack(curr, left+1, right)
                curr.pop()

            if right < left:
                curr.append(")")
                backtrack(curr, left, right+1)
                curr.pop()

        backtrack([], 0, 0)
        return answer
        