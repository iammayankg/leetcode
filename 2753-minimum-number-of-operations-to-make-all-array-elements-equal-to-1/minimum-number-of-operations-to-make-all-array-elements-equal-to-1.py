class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_ops = math.inf
        N = len(nums)
        one_count = sum(1 if num ==1 else 0 for num in nums)
        if one_count > 0:
            return N - one_count
        for i in range(N):
            g = nums[i]
            for j in range(i+1, N):
                gp = math.gcd(g, nums[j])
                if gp == 1:
                    if j-i < num_ops:
                        num_ops = j-i
                        # break
                g = gp
        return N -1 + num_ops if num_ops < math.inf else -1
        