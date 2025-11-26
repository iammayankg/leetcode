class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l, r = k, k
        currMin = nums[k]
        N = len(nums)
        ans = nums[k]
        while l > 0 or r < N-1:
            
            if l == 0:
                currMin = min(currMin, nums[r+1])
                r += 1
            elif r == N-1:
                currMin = min(currMin, nums[l-1])
                l -= 1
            elif nums[l-1] > nums[r+1]:
                currMin = min(currMin, nums[l-1])
                l -= 1
            else:
                currMin = min(currMin, nums[r+1])
                r += 1
            ans = max(ans, currMin * (r-l+1))
        return ans
        