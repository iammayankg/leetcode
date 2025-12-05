class Solution:
    def countCollisions(self, directions: str) -> int:
        N = len(directions)
        left = -1
        cnt = 0
        for d in directions:
            if d == "L":
                if left >= 0:
                    cnt += left+ 1
                    left = 0
            elif d == "S":
                if left > 0:
                    cnt += left
                left =0
            else:
                if left >= 0:
                    left += 1
                else:
                    left = 1
        return cnt





        