class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        ans = 0

        while left < right:
            l, r = height[left], height[right]
            area = min(l, r) * (right-left)
            ans = max(area, ans)
            if l < r:
                left += 1
            else:
                right -= 1
        return ans
        