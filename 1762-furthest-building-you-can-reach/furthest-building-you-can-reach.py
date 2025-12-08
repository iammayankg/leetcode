class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladderHeap = []
        N = len(heights)

        for idx, height in enumerate(heights):
            if idx < N-1:
                if heights[idx] < heights[idx+1]:
                    diff = heights[idx+1] - heights[idx]
                    heapq.heappush(ladderHeap, diff)

                    if len(ladderHeap) > ladders:
                        bricks -= heapq.heappop(ladderHeap)
                        if bricks < 0:
                            return idx
        return N-1
        