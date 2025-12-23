class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []

        maxVal = 0
        maxSum = 0

        for start, end, val in events:

            while pq and pq[0][0] < start:
                maxVal = max(maxVal, pq[0][1])
                heapq.heappop(pq)

            maxSum = max(maxSum, val + maxVal)
            heapq.heappush(pq, [end, val])

        return maxSum
        