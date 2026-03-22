class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left, right = 0, N-1
        result = [0]*N
        for i in range(N-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left]
                left += 1
            else:
                square = nums[right]
                right -= 1
            result[i] = square*square
        return result
        