class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        minHeap = []
        for i in range(ROWS):
            # soldiers_ = sum(mat[i])
            soldiers_x = bisect_left(mat[i], 0, key=lambda x: -x)
            heapq.heappush(minHeap, (soldiers_x, i))
            # if len(minHeap) > k:
            #     heapq.heappop(minHeap)
        result = []
        while minHeap and k:
            result.append(heapq.heappop(minHeap)[1])
            k -= 1
        return result
        