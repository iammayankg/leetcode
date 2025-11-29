class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N = len(seats)
        leftOrder = [-math.inf] * N
        rightOrder = [math.inf] * N
        for i in range(1,N):
            if seats[i-1] == 1:
                leftOrder[i] = i -1
            else:
                leftOrder[i] = leftOrder[i-1]
                
        for i in range(N-2, -1, -1):
            if seats[i+1] == 1:
                rightOrder[i] = i+1
            else:
                rightOrder[i] = rightOrder[i+1]
        
        result = 0
        result_dist = 0
        for i in range(N):
            if seats[i] == 1:
                continue
            toLeft = leftOrder[i]
            toRight = rightOrder[i]
            min_distance = min(i - toLeft, toRight - i)
            if min_distance > result_dist:
                result_dist = min_distance
                result = i
        return result_dist