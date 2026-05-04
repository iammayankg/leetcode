from collections import defaultdict
import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def rebalance(self):
        if len(self.maxHeap)> len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        self.rebalance()

    def findMedian(self) -> float:
        # print(self.minHeap)
        # print(self.maxHeap)
        # print("*" * 5)
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0]-self.maxHeap[0])/2
        else:
            return -self.maxHeap[0]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()