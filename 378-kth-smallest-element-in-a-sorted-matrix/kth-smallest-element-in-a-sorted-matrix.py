class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        minHeap = []
        for r in range(ROWS):
            heapq.heappush(minHeap,(matrix[r][0], r, 0))

        heapq.heapify(minHeap)

        while k-1:
            val, r, c = heapq.heappop(minHeap)
            if c < COLS-1:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+ 1))
            k -=1
        return minHeap[0][0]
        


        