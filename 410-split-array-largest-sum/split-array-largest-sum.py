class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        def nsplits(maxAllowed):
            cnt = 0
            curr = 0
            res = []
            prev_idx = 0
            for idx, num in enumerate(nums):
                if num + curr <= maxAllowed:
                    curr += num
                else:
                    res.append(nums[prev_idx:idx])
                    prev_idx = idx
                    cnt += 1
                    curr = num
            cnt += 1 if curr != 0 else 0
            res.append(nums[prev_idx:])
            return cnt, res

        low, high = max(nums), sum(nums)
        while low <= high:
            mid = (low + high)//2
            res, l = nsplits(mid)
            # if res == k:
            #     return mid
            if res > k:
                low = mid+1
            else:
                high = mid-1
        return low
        
            
        