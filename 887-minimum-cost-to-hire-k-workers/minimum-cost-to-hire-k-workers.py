class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        wage_to_quality = [(w/q, q) for q, w in zip(quality, wage)]
        wage_to_quality.sort()

        total_quality = 0
        maxHeap = []
        result = math.inf

        for rate, quality in wage_to_quality:
            heapq.heappush(maxHeap, -quality)
            total_quality += quality

            if len(maxHeap) > k:
                total_quality += heapq.heappop(maxHeap)

            if len(maxHeap) == k:
                result = min(result, total_quality*rate)

        return result        