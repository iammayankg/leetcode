class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return 1

        prefix = [1] * N
        suffix = [1] * N # Using separate lists to avoid shallow copy issues if modifying

        # Calculate prefix lengths
        for i in range(1, N):
            if nums[i] >= nums[i-1]:
                prefix[i] = prefix[i-1] + 1
            # else: prefix[i] remains 1, as a new non-decreasing subarray starts

        # Calculate suffix lengths
        for i in range(N - 2, -1, -1):
            if nums[i] <= nums[i+1]:
                suffix[i] = suffix[i+1] + 1
            # else: suffix[i] remains 1

        # Initialize result with the longest non-decreasing subarray without any replacement
        result = max(prefix)

        for i in range(N):
            # Case 1: Replace nums[i] to bridge two segments
            # Requires valid indices for i-1 and i+1, and nums[i-1] <= nums[i+1]
            if i > 0 and i < N - 1 and nums[i-1] <= nums[i+1]:
                result = max(result, prefix[i-1] + 1 + suffix[i+1])

            # Case 2: Replace nums[i] to extend a prefix segment
            # This covers scenarios like [1, 2, X] becoming [1, 2, 3]
            # where 'X' is replaced to extend [1, 2]. Length is prefix[i-1] + 1
            if i > 0:
                result = max(result, prefix[i-1] + 1)

            # Case 3: Replace nums[i] to extend a suffix segment
            # This covers scenarios like [X, 2, 3] becoming [1, 2, 3]
            # where 'X' is replaced to extend [2, 3]. Length is 1 + suffix[i+1]
            if i < N - 1:
                result = max(result, 1 + suffix[i+1])
        
        # There's a subtle edge case: if N=0 or N=1, the loop for i might not cover.
        # But for N=0, we return 0. For N=1, prefix=[1], max(prefix)=1.
        # Loop for i=0: i>0 false, i<N-1 false. So result stays 1.
        # These are handled.

        return result
