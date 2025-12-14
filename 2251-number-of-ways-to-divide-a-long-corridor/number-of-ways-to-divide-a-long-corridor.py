class Solution:
    def numberOfWays(self, corridor: str) -> int:
        count = 0
        intervals = []
        start = -1
        end = -1

        for idx, c in enumerate(corridor):
            if c == "S":
                count += 1
                if count == 1:
                    start = idx
                elif count == 2:
                    end = idx
                    intervals.append((start, end))
                    count = 0
        ways = 0
        if len(intervals) == 0 or count != 0:
            return ways
        ways = 1
        MOD = 10**9 + 7
        for i in range(1, len(intervals)):
            # if intervals[i][0] - intervals[i-1][1] <= 1:
            #     return 0
            ways *= intervals[i][0]-intervals[i-1][1]
            ways = ways % MOD
        return ways

