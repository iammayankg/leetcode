class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        countMeetings = [0]*n #Counter()
        meetings.sort()
        minHeap = []
        unusedRooms = list(range(n))
        heapq.heapify(unusedRooms)

        for start, end in meetings:
            while minHeap and minHeap[0][0] <= start:
                x = heapq.heappop(minHeap)
                heapq.heappush(unusedRooms, x[1])

            if unusedRooms:
                room = heapq.heappop(unusedRooms)
                countMeetings[room] += 1
                heapq.heappush(minHeap, (end, room))
            else:
                last_end, last_room = heapq.heappop(minHeap)
                countMeetings[last_room] += 1
                delay = abs(last_end - start)
                heapq.heappush(minHeap, (end+delay, last_room))
            

        # maxRoom = -1
        # maxCount = -1
        # for room, count in countMeetings.items():
        #     if count > maxCount:
        #         maxRoom = room
        #         maxCount = count
        return countMeetings.index(max(countMeetings))
        