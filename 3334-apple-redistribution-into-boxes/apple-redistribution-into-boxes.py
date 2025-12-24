class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        heapq._heapify_max(capacity)
        count = 0

        while total_apples > 0:
            total_apples -= heapq._heappop_max(capacity)
            count += 1
        return count
        