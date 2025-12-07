import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        minHeap = []
        for item, count in counts.items():
            heapq.heappush(minHeap, (count, item))            
            if len(minHeap) > k:
                heapq.heappop(minHeap)
                

        result = []
        while minHeap:
            c, num = heapq.heappop(minHeap)
            result.append(num)
        return result[::-1]