class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1], -x[0]))
        cnt = 0
        N = len(intervals)
        prev_start, prev_end = -1, -1
        res = []
        for start, end in intervals:
            if prev_start == -1 or start > prev_end:
                cnt += 2
                prev_start = end-1
                prev_end = end
            elif prev_start < start:
                if prev_end != end:
                    prev_start = prev_end
                    prev_end = end
                else:
                    prev_start = end-1
                    prev_end = end
                cnt += 1
        return cnt
        