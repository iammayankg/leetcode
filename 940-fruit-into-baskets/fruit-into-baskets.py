class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        window_start = 0
        res = 0
        for idx, fruit in enumerate(fruits):
            counts[fruit] += 1
            while len(counts) > 2:
                counts[fruits[window_start]] -= 1
                if counts[fruits[window_start]] == 0:
                    del counts[fruits[window_start]]
                window_start += 1
            
            res = max(res, idx - window_start + 1)
        return res


        