class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # batteries.sort()
        def check(time):
            total = 0
            for b in batteries:
                total += min(b, time)

            return total//n >= time

        low, high = min(batteries), sum(batteries)//n
        res = None
        while low <= high:
            mid = (low+high)//2
            if check(mid):
                res = mid
                low = mid + 1
            else:
                high = mid -1
        return res

        