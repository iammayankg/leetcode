class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k

        def fairDistribution(index_cookie, children, zero_count):
            if len(cookies) - index_cookie < zero_count:
                return math.inf
            if index_cookie==len(cookies):
                return max(children)
            
            minSoFar = math.inf
            for i in range(k):
                zero_count -= int(children[i] == 0) 
                children[i] += cookies[index_cookie]
                minSoFar = min(minSoFar, fairDistribution(index_cookie+1, children, zero_count))
                children[i] -= cookies[index_cookie]
                zero_count += int(children[i] == 0) 
            return minSoFar

        return fairDistribution(0, children, k)