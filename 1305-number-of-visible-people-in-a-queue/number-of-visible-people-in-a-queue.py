class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        N = len(heights)
        results = [0] * N
        stack = []

        for idx, height in enumerate(heights):
            while stack and heights[stack[-1]] < height:
                prev_index = stack.pop()
                results[prev_index] += 1
            if stack:
                results[stack[-1]] += 1
            stack.append(idx)
        return results
        